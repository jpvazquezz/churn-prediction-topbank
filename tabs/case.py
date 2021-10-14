from dash import dcc
from dash import html

layout = html.Div([
        html.H1('Business Case'),
        
        dcc.Markdown('''**Disclaimer**: the following context is fictitious and was created with educational purposes only.'''),
        dcc.Markdown('''TopBank is a large banking services company. It operates mainly in European countries offering financial products, from bank accounts to investments, passing through some types of insurance and investment product.
        The company's business model is of the service type, that is, it sells banking services to its customers through physical branches and on its website.'''),
        
        dcc.Markdown('''The company's main product is a bank account, in which the customer can deposit his salary, make withdrawals, deposits and transfer to other accounts. 
        This bank account has no cost to the customer and has a 12-month term, that is, the customer needs to renew the contract for this account to continue using it for the next 12 months.'''),

        dcc.Markdown('''According to TopBank's analytics team, each customer with a bank account returns a monetary value of 15% of their estimated salary value,
        if the salary is less than the average, and 20% if that salary is greater than the average, during the current period of their account contract. This amount is calculated annually.'''),

        dcc.Markdown('''In recent months, the Analytics team realized that the rate of customers canceling their accounts and leaving the bank, 
        reached unprecedented numbers in the company. Concerned about the increase in this rate, the team was aiming to create an action plan to reduce the customer churn rate.'''),

      	dcc.Markdown('''Generally speaking, **churn** is a metric that indicates the number of customers who canceled their contract or stopped buying your product in a given period of time. 
        For example, customers who canceled the service contract or after its expiration, did not renew, are considered churn customers.'''),

        dcc.Markdown('''One measure to tackle churning is to give clients a financial incentive so they will reconsider not renewing their contracts. Therefore
        a gift card was selected to be the financial incentive of TopBanck plan against the churning problem. However, the company can only afford to spend
        $10.000 on gift cards, which forces us to have to select only a few customer in the hopes of maximaxing the ROI (Return Over Investiment). This is where
        our task begins!'''),
        
        html.H3('The Task'),

        dcc.Markdown('''As a Data Science Consultant, I had to create an action plan to decrease the number of churn clients and show the financial return on my solution. Moreover,
        by the end, I had to deliver to TopBank's CEO a deployed model that could receive the customers' database via API and return a score to each customer, which
        represented his probability to churn. In the addition, the model had to response the resolution's financial impact.'''),

        dcc.Markdown('[ref](https://sejaumdatascientist.com/predicao-de-churn/)')

])