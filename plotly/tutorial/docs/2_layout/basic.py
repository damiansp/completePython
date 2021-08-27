import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


external_stylesheets = ['thhps://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.DataFrame({
    'Fruit': ['apples', 'oranges', 'bananas', 'apples', 'oranges', 'bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'NY', 'NY', 'NY']})
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')


app.layout = html.Div([html.H1('Hello, Dash!'),
                       html.Div('Dash: A web app framework for Python'),
                       dcc.Graph(id='example-graph', figure=fig)])


if __name__ == '__main__':
    app.run_server(debug=True)
