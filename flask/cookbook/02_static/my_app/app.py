from flask import Flask

# by default <static> dir expected to be here, but can specify a different path
app = Flask(__name__, static_folder='./static')
