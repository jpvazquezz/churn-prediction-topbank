from imblearn.over_sampling import SMOTE
from sklearn.calibration import CalibratedClassifierCV
import pickle
import pandas as pd
import numpy as np
import inflection
import xgboost as xgb

class Churn_probability(object):

    def __init__(self):
        self.home_path = ''
        self.standard_scaler = pickle.load(open(self.home_path + '\\src\\standard_scaler.pkl', 'rb'))
        self.minmax_scaler = pickle.load(open(self.home_path + '\\src\\minmax_scaler.pkl', 'rb'))
        self.robust_scaler = pickle.load(open(self.home_path + '\\src\\robust_scaler.pkl', 'rb'))
        self.init = xgb.Booster({'nthread': 4})  # init model
        self.model = self.init.load_model(self.home_path + '\\src\\model_xgb.model') #pickle.load(open(self.home_path + '\\src\\model_xgb.pkl', 'rb'))

    def get_customer_id(self, data):
        # Rename colunms
        cols_old = data.columns.to_list()
        snakecase = lambda x: inflection.underscore(x)
        cols_new = list(map(snakecase, cols_old))
        data.columns = cols_new

        # Get customer_id and the df raw
        customers_id = data['customer_id']
        df_raw = data
        return customers_id, df_raw

    def feature_engeneering(self, data):

        # Feature Engeneering - Annual Revenue
        anual_revenue = []
        for salary in data['estimated_salary']:
            if salary < data['estimated_salary'].mean():
                anual_revenue.append(salary * 0.15)
            elif salary > data['estimated_salary'].mean():
                anual_revenue.append(salary * 0.20)
        data['anual_revenue'] = pd.Series(anual_revenue)

        # Feature Filtering
        # Drop customer_id and surname
        data = data.drop(['customer_id', 'surname'], axis=1)

        return data

    def data_preparation(self, data):

        ## Categorical Variables

        # One-hot Encoding - Geography
        data = pd.get_dummies(data, prefix=['geography'], columns=['geography'])

        # Label encoding - Gender
        data['gender'] = [1 if gender == 'Male' else 2 for gender in data['gender']]

        ## Numerical Variables

        # Normalization - Almost normal distribution features
        data['age'] = self.standard_scaler.fit_transform(data[['age']].values)
        data['credit_score'] = self.standard_scaler.fit_transform(data[['credit_score']].values)

        # Rescaling - Non-Normal distribuited features
        data['tenure'] = self.minmax_scaler.fit_transform(data[['tenure']].values)
        data['estimated_salary'] = self.minmax_scaler.fit_transform(data[['estimated_salary']].values)
        data['anual_revenue'] = self.minmax_scaler.fit_transform(data[['anual_revenue']].values)

        # Robust Scaler
        data['balance'] = self.robust_scaler.fit_transform(data[['balance']].values)

        return data

    def data_balacing(self, data):
        # Data Balacing using SMOTE
        smote = SMOTE(random_state=42)
        X_smote, y_smote = smote.fit_resample(data.loc[:, data.columns != 'exited'], data.exited)

        # Already balanced X and Y
        X = X_smote
        y = y_smote

        return X, y

    def get_proba(self, data, X, y):
        ## CALIBRATION WITH CalibratedClassifierCV
        calibration = CalibratedClassifierCV(self.model, method='sigmoid', cv=5)
        calibration.fit(X, y)

        # Predict probabilities for THE WHOLE DATASET
        prob_xgb_full = calibration.predict_proba(data[X.columns])[:, 1]

        return prob_xgb_full

    def get_df_prob(self, customer_id, df_raw, prob):
        df_raw['customer_id'] = customer_id
        df_raw['prob'] = prob
        df_prob = df_raw
        return df_prob

    def get_gifted_customers(self, df_prob, limited_budget):
        # Creating a Dataframe with only the churned clients
        df_prob_churn = df_prob[df_prob.exited == 1]

        # Creating a DataFrame with the probabilities to churn, the LTV, the gift cost and the ROI
        df_result = pd.DataFrame()
        df_result['customer_id'] = df_prob_churn.customer_id
        df_result['prob'] = df_prob_churn.prob
        df_result['LTV'] = df_prob_churn.anual_revenue

        conditions = [
            (df_result['prob'] >= 0.9),
            (df_result['prob'] >= 0.8) & (df_result['prob'] < 0.9),
            (df_result['prob'] >= 0.75) & (df_result['prob'] < 0.8),
            (df_result['prob'] < 0.75)
        ]
        cost = [np.nan, 200, 100, 50]

        # Designate gift cost according to churn probabilities
        df_result['gift_cost'] = np.select(conditions, cost)

        # Calculate the ROI (LTV - gift cost)
        df_result['ROI'] = df_result.LTV - df_result.gift_cost

        # Select only the clients that may not churn and sort by the ROI
        selected_gifts = df_result.loc[(df_result.prob > 0.7) & (df_result.prob < 0.9)].sort_values(['ROI'],
                                                                                                    ascending=False)

        # Selecting the customers to receive the gift card according to the limited budget
        total_sum = 0
        customers = []

        for customer, gift in zip(selected_gifts.customer_id, selected_gifts.gift_cost):
            total_sum = total_sum + gift
            # Selection goes up to the amount of gift card we can spend, which is $10.000
            if total_sum > limited_budget:
                break
            # Add client to list
            customers.append(customer)

        # Create final Dataframe
        gifted_customers = selected_gifts[selected_gifts.customer_id.isin(customers)]

        return gifted_customers

# C:\\Users\\Dell\\Desktop\\ciencia_de_dados\\0.Comunidade DS\\PA_03