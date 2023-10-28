import requests

from . import app
from .models import Impression


def job_1():
    i = Impression()
    print(i)

    response = requests.post(f"{app.config['BIDDER_ADDR']}new-imp",
                             json={'id': str(i.id), 'profile': i.profile})
    if response.status_code == requests.codes.ok:
        i_bid = response.json()
        print(f"Received bid of {i_bid['bid']} for impression {i_bid['id']}")
