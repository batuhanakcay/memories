import flask


app = flask.Flask(__name__)

app.config.from_object('memories.config')

app.config.from_envvar('MEMORIES_SETTINGS', silent=True)

import memories.views
import memories.model  
