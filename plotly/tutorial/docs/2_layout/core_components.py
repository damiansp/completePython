import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

options=[{'label': 'New York City', 'value': 'NYC'},
         {'label': u'Montréal', 'value': 'MTL'},
         {'label': 'San Francisco', 'value': 'SF'}]
app.layout = html.Div(
    [
        html.Label('Dropdown'),
        dcc.Dropdown(options=options, value='MTL'),

        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(options=options, value=['MTL', 'SF'], multi=True),

        html.Label('Radio Items'),
        dcc.RadioItems(options=options, value='MTL'),

        html.Label('Checkboxes'),
        dcc.Checklist(options=options, value=['MTL', 'SF']),

        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5)
    ], style={'columnsCount': 2})


if __name__ == '__main__':
    app.run_server(debug=True)
                      
