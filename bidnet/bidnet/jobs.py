from flask_apscheduler import APScheduler

from . import app

scheduler = APScheduler()
scheduler.init_app(app)


@scheduler.task('interval', id='job_1', seconds=15, misfire_grace_time=900)
def job_1():
    print('Job 1 executed')


scheduler.start()
