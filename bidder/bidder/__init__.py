import requests

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from ..config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from . import routes, models

response = requests.get(f"{app.config['BIDNET_ADDR']}start")
if response.status_code == requests.codes.ok:
    print(f"bidnet: {response.json().get('job')} created")


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Impression': models.Impression}
