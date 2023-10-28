import requests

from . import app
from .models import Impression


def job_1():
    i = Impression()
    requests.post(f"{app.config['BIDDER_ADDR']}new-imp", i.profile)
    print(i)
