import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotyly.express as px


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)

df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
available_indicators = df['Indicator Name'].unique()


app.layout = html.Div([
    html.Div(
        [html.Div(
            [dcc.Dropdown(
                id='crossfilter-xaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='Fertility rate, total (births per woman)'),
             dcc.RadioItems(
                 id='crossfilter-xaxis-type',
                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                 value='Linear',
                 labelStyle={'display': 'inline-block', 'marginTop': '5px'})],
            style={'width': '49%', 'display': 'inline-block'}),
         html.Div(
             [dcc.Dropdown(
                 id='crossfilter-yaxis-column',
                 options=[{'label': i, 'value': i}
                          for i in available_indicators],
                 value='Life exp. at birth, total (years)'),
              dcc.RadioItems(
                  id='crossfilter-yaxis-type',
                  opions=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                  value='Linear',
                  labelStyle={'display': 'inline-block', 'marginTop': '5px'})],
             style={
                 'width': '49%', 'float': 'right', 'display': 'inline-block'})],
        style={'padding': '10px 5px'}),
    html.Div(
        [dcc.Graph(id='crossfilter-indicator-scatter',
                   hoverData={'points': [{'customdata': 'Japan'}]})],
        style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    html.Div([dcc.Graph(id='x-time-series'), dcc.Graph(id='y-time-series')],
             style={'display': 'inline-block', 'width': '49%'}),
    html.Div(
        dcc.Slider(id='crossfilter-year-slider',
                   min=df.Year.min(),
                   max=df.Year.max(),
                   value=df.Year.max(),
                   marks={str(year): str(year) for year in df.Year.unique()},
                   step=None),
        style={'width': '49%', 'padding': '0px 20px 20px 20px'})])


@app.callback(Output('crossfilter-indicator-scatter', 'figure'),
              [Input('crossfilter-xaxis-column', 'value'),
               Input('crossfilter-yaxis-column', 'value'),
               Input('crossfilter-xaxis-type', 'value'),
               Input('crossfilter-yaxis-type', 'value'),
               Input('crossfilter-year-slider', 'value')])
def update_graph(x_name, y_name, x_type, y_type, year):
    dff = df[df.Year == year]
    fig = px.scatter(
        x=dff[dff['Indicator Name'] == x_name]['Value'],
        y=dff[dff['Indicator Name'] == y_name]['Value'],
        hover_name=dff[dff['Indicator Name'] == y_name]['Country Name'])
    fig.update_traces(
        customdata=dff[dff['Indicator Name'] == y_name]['Country Name'])
    fig.update_xaxes(title=x_name,
                     type='linear' if x_type == 'Linear' else 'log')
    fig.update_yaxes(title=y_name,
                     type='linear' if x_type == 'Linear' else 'log')
    
    
