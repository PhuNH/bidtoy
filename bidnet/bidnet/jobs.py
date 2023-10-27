import random
import string

from flask_apscheduler import APScheduler

from . import app, db
from .models import Impression

scheduler = APScheduler()
scheduler.init_app(app)


def profile_generator(length=5):
    profile = ''.join([random.choice(string.ascii_lowercase) for _ in range(length)])
    return profile


@scheduler.task('interval', id='job_1', seconds=5, misfire_grace_time=900)
def job_1():
    with app.app_context():
        i = Impression(profile=profile_generator(20))
        db.session.add(i)
        db.session.commit()
        print(i)


scheduler.start()
