import dash
from dash.dependencies import Input, Output, State
from dash import dcc 
from dash import html
from dash.exceptions import PreventUpdate
from dash import dash_table

from tabs import case, churn_prob, about

import pandas as pd
import base64
import io
from churnprobability.ChurnProbability import Churn_probability

df = pd.read_csv('churn.csv')
df.drop('RowNumber', axis=1, inplace=True)


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
style = {'maxWidth': '960px', 'margin': 'auto'}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server

app.layout = html.Div([
    html.H1('Churn Probability Detection - TopBank'),
    dcc.Tabs(id="tabs", value='tab-churn',children=[
        dcc.Tab(label='Churn Probability', value='tab-churn'),
        dcc.Tab(label='Bussiness Case', value='tab-case'),
        dcc.Tab(label='About the app', value='tab-app')
    ]),
    html.Div(id='tabs-content')
], style=style)

@app.callback(Output('tabs-content','children'),
			  [Input('tabs', 'value')])
def render_content(tab):
	if tab == 'tab-churn':
		return churn_prob.layout
	elif tab == 'tab-case':
		return case.layout	
	elif tab == 'tab-app':
		return about.layout

@app.callback(Output('loading-output-1','children'),
				[State('input-budget','value'),Input('upload-csv','contents')])

def upload_churn(input_budget, contents):

	if input_budget is None:
		raise PreventUpdate

	content_type, content_string = contents.split(',')
	decoded = base64.b64decode(content_string)

	if decoded is not None:

		dataframe = pd.read_csv(io.StringIO(decoded.decode('utf-8')))

		churn = Churn_probability()
		customers_id, df_raw = churn.get_customer_id(dataframe)

		data = churn.feature_engeneering(dataframe)
		data = churn.data_preparation(data)
		X,y = churn.data_balacing(data)
		churn_probabilitis = churn.get_proba(data, X,y)
		df_prob = churn.get_df_prob(customers_id, df_raw, churn_probabilitis)
		gifted_customers = churn.get_gifted_customers(df_prob, input_budget)

		
		return html.Div([
				dcc.Markdown('\n**Top 10 customers with the highest ROI (Return Over Investment)**\n'),

				dash_table.DataTable(data=gifted_customers.head(10).to_dict('records'), columns=[{'name': i, 'id': i} for i in gifted_customers.columns]),

				dcc.Markdown('\n**Financial Impact**'),

                dcc.Markdown('The financial incentive (gift card) included {} customers from the total {} customers in churn.'.format(
                    gifted_customers.customer_id.nunique(), df_prob[df_prob.exited == 1].shape[0])),

            	dcc.Markdown('It could be expected to return a ROI of ${:,.2f}.'.format(gifted_customers.ROI.sum().round(2))),

            	dcc.Markdown('The total lost revenue if we expect all customers to churn would be ${:,.2f}. This means that we could save {:.0%} of revenue from using this model to prevent customers to churn.'.format(
                    df_prob[df_prob.exited == 1].anual_revenue.sum().round(2),
                        gifted_customers.ROI.sum().round(2) / df_prob[df_prob.exited == 1].anual_revenue.sum().round(2)))
            ])



@app.callback(Output('loading-output-2','children'),
				[State('input-budget','value'),Input('default-csv','n_clicks')])
def default_churn(input_budget, n_clicks):
	if input_budget is None:
		raise PreventUpdate

	if n_clicks is not None:

		churn = Churn_probability()
		customers_id, df_raw = churn.get_customer_id(df)

		data = churn.feature_engeneering(df)
		data = churn.data_preparation(data)
		X,y = churn.data_balacing(data)
		churn_probabilitis = churn.get_proba(data, X,y)
		df_prob = churn.get_df_prob(customers_id, df_raw, churn_probabilitis)
		gifted_customers = churn.get_gifted_customers(df_prob, input_budget)

		
		return html.Div([
				dcc.Markdown('\n**Top 10 customers with the highest ROI (Return Over Investment)**\n'),

				dash_table.DataTable(data=gifted_customers.head(10).to_dict('records'), columns=[{'name': i, 'id': i} for i in gifted_customers.columns]),

				dcc.Markdown('\n**Financial Impact**'),

                dcc.Markdown('The financial incentive (gift card) included {} customers from the total {} customers in churn.'.format(
                    gifted_customers.customer_id.nunique(), df_prob[df_prob.exited == 1].shape[0])),

            	dcc.Markdown('It could be expected to return a ROI of ${:,.2f}.'.format(gifted_customers.ROI.sum().round(2))),

            	dcc.Markdown('The total lost revenue if we expect all customers to churn would be ${:,.2f}. This means that we could save {:.0%} of revenue from using this model to prevent customers to churn.'.format(
                    df_prob[df_prob.exited == 1].anual_revenue.sum().round(2),
                        gifted_customers.ROI.sum().round(2) / df_prob[df_prob.exited == 1].anual_revenue.sum().round(2)))
            ])



if __name__ == '__main__':
	app.run_server(debug=True)


### Structuring the multi-tab app
# https://community.plotly.com/t/structuring-a-multi-tab-app/13331