import requests

from . import app
from .models import Impression


def job_1():
    i = Impression()
    print(i)

    response = requests.post(f"{app.config['BIDDER_ADDR']}imp",
                             json={'id': str(i.id), 'profile': i.profile})
    if response.status_code == requests.codes.ok:
        i_bid = response.json()
        print(f"Received bid of {i_bid['bid']} for impression {i_bid['id']}")
        # Whether the bidder wins the impression, tells it
        is_won = int(i_bid['bid']) > 0
        requests.put(f"{app.config['BIDDER_ADDR']}imp/{str(i.id)}",
                     json={'is_won': is_won})
