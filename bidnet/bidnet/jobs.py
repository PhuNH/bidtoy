import requests

from . import app
from .models import Impression


def job_1():
    i = Impression()
    print(i)

    response = requests.post(f"{app.config['BIDDER_ADDR']}new-imp", i.profile)
    if response.status_code == requests.codes.ok:
        bid = response.content
        print(f'Received bid of {bid}')
