# Churn Prediction Probability - TopBank
## An action plan based upon detecting TopBank customers' churn probability

![](https://www.milldesk.com.br/wp-content/uploads/2019/09/customer-churn-milldesk-1024x513.jpeg)

## 1. Business Problem

TopBank is a large banking services company that operates mainly in European countries offering financial products, from bank accounts to investments, passing through some types of insurance and investment product. The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. This bank account has a 12-month term, that is, the customer needs to renew the account contract to continue using it for the next 12 months.

In recent months, the Analytics team realized that the rate of customers canceling their accounts and leaving the bank or not renewing their contracts reached unprecedented numbers in the company. Generally speaking, **churn** is the metric that indicates the number of customers who canceled their contract or stopped buying your product in a given period of time. 

 As a Data Science Consultant, I had to create an action plan to decrease the number of churn clients and show the financial return on my solution. Moreover, by the end, I had to deliver to TopBank's CEO a deployed model that could receive the customers' database via API and return a score to each customer, which represented his probability to churn. In the addition, the model had to response the resolution's financial impact.

## 2. Business Assumptions

- **TopBank's revenue**: According to TopBank's analytics team, each customer with a bank account returns a monetary value of 15% of their estimated salary value if the salary is less than the average, and 20% if that salary is greater than the average, during the current period of their account contract. This amount is calculated annually.

- **Churn combat approach**: One measure to tackle churning is to give clients a financial incentive so they will consider renewing their contracts. In our case, **gifts cards** were selected to be the financial incentive of TopBank plan against the churning problem.

- **Financial incentive budget**: the company can only afford to spend $10.000 on gift cards, which forces us to have to select only a few customers in order to maximaxe the ROI (Return Over Investiment).

- **Gift cards destination**: in a realistic scenario where we have limited budget, I assumed that the gift cards values had to vary according to the customer probability to churn:
	- Customers that would churn no matter how high the incentive: p(churn) > 0\.90
	- Customers that may not churn, but only with a $200 gift card: 0\.80 < p(churn) < 0.89
	- Customers that may not churn with a $100 gift card: 0\.75 < p(churn) < 0.79
	- Customers that may not churn with a $50 gift card: p(churn) < 0\.75


## 3. Solution Strategy
The solution was based upon the following strategy:

1. **Step 1 - Data Description**: use descriptive statistics to identify important or ususual behaviours in the data.
2. **Step 2 - Feature Engeering**: create or derive new variables to help better understand the phenomenon or to improve model performance.
3. **Step 3 - Feature Filtering**: filter the unnecessary variables and row in terms of information gain of that are outside the business' scope.
4. **Step 4 - Exploratory Data Analysis**: explore the data to find insights, to comprehend the variables' behaviour and their consequent impact on the model's learning. 
5. **Step 5 - Data Preparation**: use techniques to better prepare the data to the machine learning model. 
6. **Step 6 - Feature Selection**: select the features that contain the main information and attributes requeried from the model to learn the the phenomenon's behaviour. 
7. **Step 7 - Machine Learning Modelling**: machine learning model training and performance comparasion. 
8. **Step 8 - Churn Analysis**: analyse the churn probability of TopBank's customers
9. **Step 9 - Bussiness Report and Financial Impact**: find out what is the financial impact if the model is implemented to avoid customer churn.
10. **Step 10 - Deploy**: deploy the model in production. 

## 4. Top 3 Data Insights:
	
**Hypothesis 1**: the higher the salary, the higher the balance.

R: False, there is no evidence to support this hypothesis.

**Hypothesis 2**: the greater the number of products, the higher the revenue.

R: False, there is no evidence to support this hypothesis.

**Hypothesis 3**: The more years the customer has in the bank, the higher his balance.

R: False, there is no evidence to support this hypothesis.

## 5. Machine Leaning Model Application:
The following classification algorithms were tested:

- Logistic Regression
- SVC
- XGBoost Classifier
- Random Forest Classifier

F1-Score was elected the main metric of performance evaluation. Morover, the calibration curve was also used as a technique to elect the best model. 

|          |  Logistic Regression  |       SVC        |     XGBoost     |   Random Forest  | 
|----------|-----------------------|------------------|-----------------|------------------|
| F1-Score |    0\.713+/-0\.014    | 0\.803+/-0\.016  | 0\.901+/-0\.008 |   0\.887+/-0\.01 |

## 6. Machine Learning Performance

The **XGBoost** was the chosen algorithm to be applied. In addition, I made a calibration using CalibratedClassifierCV.	
The table shows the F1-Score metric after running a cross validation score with 10 splits in the full dataset.
Model's final performance:

| Chosen Model | F1-Score |
|--------------|----------|
|    XGBoost   |  0\.905  |

## 7. Business Results

The financial incentive (gift card) included **70 customers** from the total 2037 customers in churn.

It could be expected to return a ROI of **$2,635,998.25**.

The **total lost revenue** if we expect all customers to churn would be **$38,846,324.63**. This means that we could **save up to 7% of revenue** from using this model to prevent customers to churn.

## 8. Conclusions

By the end of the project, I was able to create a XGBoost model that predicted the TopBank customers' probability to churn and also formulate a action plan to tackle the churning problem based on giving customers a gift card in accordance to their churn probability and the maximization of customers' ROI. In addition to the financial return, the model was created using Dash and deployed in production with Heroku.

## 9. Lessons Learned
- Extremely low correlation between features 
- Managing imbalanced data with SMOTE
- Utilizing Calibration Curve as a criteria to elect the best model
- Dash framework 


## 10. To Improve
- Improve feature engeenering (elaborate more features)
- Create a better algorithm to select the customers
- Do hyperparameter fine-tunning
- Improve Dash app UX

## About the author

This project is powered by DS Community. DS Community is a data science hub designed to forge elite data scientists based on real bussiness solutions and practical projects. To know more about DS Community, click [here](https://www.comunidadedatascience.com/).

To check out the app, **click [here](https://churn-prediction-topbank.herokuapp.com/)**.

The solution was created by **João Pedro Vazquez**. Graduated as a political scientist, João Pedro is an aspiring data scientist, who seeks to improve his skills through projects with real bussiness purposes and through continuous and sharpened study.

[<img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"/>](https://www.linkedin.com/in/joao-pedro-vazquez/) [<img alt="Medium" src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"/>](https://jpvazquez.medium.com/) [<img alt="Microsoft Outlook" src="https://img.shields.io/badge/Microsoft_Outlook-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white"/>](jpvazquezz@hotmail.com)
