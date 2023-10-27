from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from ..config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy()
db.init_app(app)
migrate = Migrate(app, db)

from . import routes, jobs, models


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Impression': models.Impression, 'Bidder': models.Bidder}
