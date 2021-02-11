from flask import Flask


app = Flask(__name___)
app.config['DEBUG'] = True # or
DEBUG = True
TESTING = True             # or
app.config.from_pyfile('myconfig.cfg') # or...
app.config.from_object('multi_config.DevConfig') # ...
app.config.from_object(__name__)
app.config.from_envvar('PATH_TO_CONFIG_FILE')
