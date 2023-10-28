from flask import request, jsonify

from . import app, scheduler
from .jobs import job_1


@app.route('/')
def index():
    return 'Welcome to bidnet!'


@app.route('/start')
def start():
    job = scheduler.add_job(
        func=job_1,
        trigger='interval',
        seconds=5,
        id='job_1',
        replace_existing=True
    )
    return jsonify({'remote_addr': request.remote_addr, 'job': job.id}), 200
