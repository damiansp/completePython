import ssl

import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

ssl._create_default_https_context = ssl._create_unverified_context


app = dash.Dash(__name__)
df = pd.read_csv('https://plotly.github.io/datasets/country_indicators.csv')
available_indicators = df['Indicator Name'].unique()


def log_linear_radio(id):
    return dcc.RadioItems(
        id=id,
        options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
        value='Linear',
        labelStyle={'display': 'inline-block'})


app.layout = html.Div([
    html.Div([
        html.Div(
            [dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='Fertility rate, total (births per woman)'),
             log_linear_radio('xaxis-type')],
            style={'width': '48%', 'display': 'inline-block'}),
        html.Div(
            [dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i}
                         for i in available_indicators],
                value='Life expectancy at birth, total (years)'),
             log_linear_radio('yaxis-type')],
            style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),
    dcc.Graph(id='indicator-graphic'),
    dcc.Slider(id='year-slider',
               min=df.Year.min(),
               max=df.Year.max(),
               value=df.Year.min(),
               marks={str(year): str(year) for year in df.Year.unique()})])


@app.callback(Output('indicator-graphic', 'figure'),
              Input('xaxis-column', 'value'),
              Input('yaxis-column', 'value'),
              Input('xaxis-type', 'value'),
              Input('yaxis-type', 'value'),
              Input('year-slider', 'value'))
def update_graph(xcol_name, ycol_name, xtype, ytype, year):
    dff = df[df.Year == year]
    fig = px.scatter(
        x=dff[dff['Indicator Name'] == xcol_name]['Value'],
        y=dff[dff['Indicator Name'] == ycol_name]['Value'],
        hover_name=dff[dff['Indicator Name'] == ycol_name]['Country Name'])
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                      hovermode='closest')
    fig.update_xaxes(title=xcol_name,
                     type='linear' if xtype == 'Linear' else 'log')
    fig.update_yaxes(title=ycol_name,
                     type='linear' if ytype == 'Linear' else 'log')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
