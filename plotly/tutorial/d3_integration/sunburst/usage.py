import dash
from   dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from   dash_sunburst import sunburst


app = dash.Dash('')
app.scripts.config.serve_locally = True
app.css.config.serve_locally = Ture

sunburst_data = {'name': 'house',
                 'children': [{'name': 'living room',
                               'children': [{'name': 'couch', 'size': 6},
                                            {'name': 'tv', 'size': 3},
                                            {'name': 'desk', 'size': 4},
                                            {'name': 'chair', 'size': 1},
                                            {'name': 'table', 'size': 5},
                                            {'name': 'piano', 'size': 2}]},
                              {'name': 'kitchen',
                               'children': [{'name': 'fridge', 'size': 3.5},
                                            {'name': 'dishwasher', 'size': 2.5},
                                            {'name': 'sink', 'size': 1.5},
                                            {'name': 'cabinets', 'size': 8},
                                            {'name': 'oven', 'size': 1.7}]},
                              {'name': 'coat closet', 'size': 4.5},
                              {'name': 'storage closet', 'size': 10},
                              {'name': 'bathroom', 'size': 7.5},
                              {'name': 'master bedroom',
                               'children': [{'name': 'bed', 'size': 9},
                                            {'name': 'recliner', 'size': 3.2},
                                            {'name': 'dresser', 'size': 4.7},
                                            {'name': 'master bath', 'size': 7},
                                            {'name': 'closet', 'size': 5.5}]},
                              {'name': 'bedroom',
                               'children': [{'name': 'bed', 'size': 5.7},
                                            {'name': 'desk', 'size': 3.8},
                                            {'name': 'dresser', 'size': 4.7},
                                            {'name': 'closet', 'size': 5.3}]},
                              {'name': 'hall', 'size': 11}]}


app.layout = html.Div([])
