from flask import Flask


app = Flask(__name___)
app.config['DEBUG'] = True
app.config.from_pyfile('myconfig.cfg')
app.config.from_object('myapp.default_settings')
app.config.from_object(__name__)
app.config.from_envvar('PATH_TO_CONFIG_FILE')
