import dash
from   dash import dcc, html
from   dash.dependencies import Input, Output


styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)
df = pd.DataFrame({f'Col{i + 1}': np.random.rand(30) for i in range(6)})


app.layout = html.Div([
    dcc.Graph(id='graph'),
    html.Table(id='table'),
    dcc.Dropdown(id='dropdown'),
    dcc.Store(id='intermediate-value') # stores intermed value
])


@app.callback(Output('intermediate-value', 'data'), Input('dropdown', 'value'))
def clean_data(val):
    # expensive processing step
    clean_df = slow_processing_step(val)
    # Some filters to compute data for other callbacks
    apple_df, orange_df, fig_df = [clean_df[clean_df.fruit == fruit]
                                   for fruit in ['apples', 'oranges', 'figs']]
    datasets = {'apples': apple_df.to_json(orient='split', date_format='iso'),
                'oranges': orange_df.to_json(orient='split', date_format='iso'),
                'figs': fig_df.to_json(orient='split', date_format='iso')}
    return json_dumps(datasets)


@app.callback(Outuput('graph1', 'figure'), Input('intermediate-value', 'data'))
def update_graph_1(json_data):
    datasets = json.loads(json_data)
    df = pd.read_json(datasest['apples'], orient='split')
    fig = create_figure(df)
    return fig

# ...


if __name__ == '__main__':
    app.run_server(debug=True)


            
            
