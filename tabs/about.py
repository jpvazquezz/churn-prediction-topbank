from dash import dcc
from dash import html

layout = html.Div([

		html.H1('About the app'),

		dcc.Markdown('''And there you had it! The model was built with XGBoost to predict the customers' probability to churn, using
            Dash to create the web app interface, deployed with Heroku. The data used to create the solution is available on [Kaggle](https://www.kaggle.com/mervetorkan/churndataset).'''),

		dcc.Markdown('''This project is powered by DS Community. DS Community is a data science hub designed to forge elite data scientists based on
		real bussiness solutions and practical projects. To know more about DS Community, check it out [here](https://www.comunidadedatascience.com/).  
		'''),

		dcc.Markdown('''The solution was created by **João Pedro Vazquez**. Graduated as a political scientist, João Pedro is an aspiring data scientist,
			who seeks to improve his skills through projects with real bussiness purposes and through continuous and sharpened study.'''),

		dcc.Markdown('''[LinkedIn](https://www.linkedin.com/in/joao-pedro-vazquez/)
						[GitHub](https://github.com/jpvazquezz)	''')

	])