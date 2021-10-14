import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output



layout = html.Div([
			html.H6('''This API aims to identify which customers, that have high probability to churn, should be
        selected to receive a financial incentive, which in this case is a gift card, in the hopes that TopBank can still
        maintain these clients in our company.
        '''),
			dcc.Markdown('Please insert the budget for the financial incentive:'),
			dcc.Input(id='input-budget', type='number'),

			dcc.Markdown('Please upload a CSV file: '),
			dcc.Upload(children=html.Button('Upload CSV file'), id='upload-csv'),

			dcc.Markdown('Or use default data:'),
    		html.Button('Upload default data', id='default-csv',n_clicks=0),

    		dcc.Loading(
            id="loading-1",
            type="default",
            children=html.Div(id="loading-output-1")),

    		dcc.Loading(
            id="loading-2",
            type="default",
            children=html.Div(id="loading-output-2")
        )
	])
