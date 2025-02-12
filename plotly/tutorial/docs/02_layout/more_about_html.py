# -*- encoding: utf-8 -*-

# > python3 app.py
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {'background': '#111111', 'text': '#7FDBFF'}

df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples','Oranges', 'Bananas'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['SF', 'SF', 'SF', 'NY', 'NY', 'NY']})
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')
fig.update_layout(plot_bgcolor=colors['background'],
                  paper_bgcolor=colors['background'],
                  font_color=colors['text'])

app.layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.H1(children='Hello, Dash!',
                style={'textAlign': 'center', 'color': colors['text']}),
        html.Div(children='Dash: A Python web app framework.',
                 style={'textAlign': 'center', 'color': colors['text']}),
        dcc.Graph(id='example-graph-2', figure=fig)])


if __name__ == '__main__':
    app.run_server(debug=True)
