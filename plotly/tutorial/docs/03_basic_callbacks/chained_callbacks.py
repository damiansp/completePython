# -*- coding: utf-8 -*-
import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)

all_options = {'America': ['NYC', 'SF', 'Cinci'],
               'Cananda': ['Montreal', 'Toronto', 'Ottawa']}
app.layout = html.Div([
    dcc.RadioItems(id='countries-radio',
                   options=[{'label': k, 'value': k} for k in all_options],
                   value='America'),
    html.Hr(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values')])


@app.callback(Output('cities-radio', 'options'),
              Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]


@app.callback(Output('cities-radio', 'value'),
              Input('countries-radio', 'value'))
def set_cities_value(available_options):
    return available_options[0]['value']


@app.callback(Output('display-selected-values', 'children'),
              Input('countries-radio', 'value'),
              Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} is a city in {selected_country}'


if __name__ == '__main__':
    app.run_server(debug=True)
               
