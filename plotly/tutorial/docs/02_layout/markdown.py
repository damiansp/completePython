import dash
import dash_core_components as dcc
import dash_html_components as html

styles = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=styles)
markdown = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/) specifications.
Check out the [60 second tutorial there](http://commonmark.org/help/)!
'''

app.layout = html.Div([dcc.Markdown(children=markdown)])


if __name__ == '__main__':
    app.run_server(debug=True)
