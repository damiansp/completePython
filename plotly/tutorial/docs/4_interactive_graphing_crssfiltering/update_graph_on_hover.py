import ssl

import dash
from   dash import dcc, html
from   dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

ssl._create_default_https_context = ssl._create_unverified_context
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
                 value='Life expectancy at birth, total (years)'),
              dcc.RadioItems(
                  id='crossfilter-yaxis-type',
                  options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
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
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
                      hovermode='closest')
    return fig


def create_timeseries(df, axis_type, title):
    fig = px.scatter(df, x='Year', y='Value')
    fig.update_traces(mode='lines+markers')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(type='linear' if axis_type == 'Linear' else 'log')
    fig.add_annotation(x=0,
                       y=0.85,
                       xanchor='left',
                       yanchor='bottom',
                       xref='paper',
                       yref='paper',
                       showarrow=False,
                       align='left',
                       text=title)
    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 't': 10, 'r': 10})
    return fig


@app.callback(Output('x-time-series', 'figure'),
              [Input('crossfilter-indicator-scatter', 'hoverData'),
               Input('crossfilter-xaxis-column', 'value'),
               Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hover_data, x_name, ax_type):
    country_name = hover_data['points'][0]['customdata']
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == x_name]
    title = f'<b>{country_name}</b><br />{x_name}'
    return create_timeseries(dff, ax_type, title)


@app.callback(Output('y-time-series', 'figure'),
              [Input('crossfilter-indicator-scatter', 'hoverData'),
               Input('crossfilter-yaxis-column', 'value'),
               Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hover_data, y_name, ax_type):
    dff = df[df['Country Name'] == hover_data['points'][0]['customdata']]
    dff = dff[dff['Indicator Name'] == y_name]
    return create_timeseries(dff, ax_type, y_name)


if __name__ == '__main__':
    app.run_server(debug=True)
