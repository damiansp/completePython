import json

import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


style = 'https://codepen.io/chriddyp/pen/bWLwgP.css'
app = dash.Dash(__name__, external_stylesheets=[style])

styles = {'pre': {'border': 'thin lightgrey solid', 'overflowX': 'scroll'}}
df = pd.DataFrame({'x': [0.538, 0.673, 0.173, 0.686],
                   'y': [0.246, 0.428, 0.035, 0.562],
                   'custom_data': [1, 2, 3, 4],
                   'fruit': ['apple', 'apple', 'orange', 'orange']})
fig = px.scatter(df, x='x', y='y', color='fruit', custom_data=['custom_data'])
fig.update_layout(clickmode='event+select')
fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(id='basic-interactions', figure=fig),
    html.Div(
        className='row',
        children=[
            html.Div(
                [
                    dcc.Markdown(
                        '''
                        **Hover Data**
                        
                        Mouse overs values in the graph'''),
                    html.Pre(id='hover-data', style=styles['pre'])
                ],
                className='three columns'),
            html.Div(
                [
                    dcc.Markdown(
                        '''
                        **Click Data**

                        Click on points int the graph'''),
                    html.Pre(id='click-data', style=styles['pre']),
                ],
                className='three columns'),
            html.Div(
                [
                    dcc.Markdown(
                        '''
                        **Selection Data**

                        Choose the lasso or rectangle tool in the graph menu bar
                        and then select points in the graph.

                        Note that if `layout.clickmode = 'event+select'`, 
                        selection data also accumulates (or unaccumulates) 
                        selected dat if you hold down the shift button while
                        clicking.'''),
                    html.Pre(id='selected-data', style=styles['pre']),
                ],
                className='three columns'),
            html.Div(
                [
                    dcc.Markdown(
                        '''
                        **Zoom and Relayout Data**

                        Click and drag on the graph to zoom or click on the 
                        zoom buttonsin ght graph menu bar. Clicking on legend
                        items will also fire this event.'''),
                    html.Pre(id='relayout-data', style=styles['pre']),
                ],
                className='three columns')])])


@app.callback(Output('hover-data', 'children'),
              Input('basic-interactions', 'hoverData'))
def display_hover_data(hover_data):
    return json.dump(hover_data, indent=2)


@app.callback(Output('click-data', 'children'),
              Input('basic-interactions', 'clickData'))
def display_click_data(click_data):
    return json.dumps(click_data, indent=2)


@app.callback(Output('selected-data', 'children'),
              Input('basic-interactions', 'selectedData'))
def display_selected_data(selected):
    return json.dumps(selected, indent=2)


@app.callback(Output('relayout-data', 'children'),
              Input('basic-interactions', 'relayoutData'))
def display_relayout_data(relayout):
    return json.dumps(relayout, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)
                        
                     
