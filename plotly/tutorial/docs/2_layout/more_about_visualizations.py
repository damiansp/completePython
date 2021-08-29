import ssl

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

ssl._create_default_https_context = ssl._create_unverified_context


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)
data_url = ('https://gist.githubusercontent.com/chriddyp/'
            '5d1ea79569ed194d432e56108a04d188/raw/'
            'a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df = pd.read_csv(data_url)
fig = px.scatter(df,
                 x='gdp per capita',
                 y='life expectancy',
                 size='population',
                 color='continent',
                 hover_name='country',
                 log_x=True,
                 size_max=60)

app.layout = html.Div([dcc.Graph(id='graph', figure=fig)])


if __name__ == '__main__':
    app.run_server(debug=True)
