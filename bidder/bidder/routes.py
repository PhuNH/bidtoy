from flask import request

from . import app, db
from .models import Impression


@app.route('/')
def index():
    return 'Welcome to bidder'


def calc_bid(imp_profile: str) -> int:
    bidder_profile = app.config['PROFILE']
    print(f"Bidder: '{bidder_profile}'; Impression: '{imp_profile}'")
    return 10


@app.route('/new-imp', methods=['POST'])
def receive_imp():
    imp_profile = request.data.decode('ascii')
    bid = calc_bid(imp_profile)
    # db.session.add(Impression(profile=imp_profile, bid=bid))
    return str(bid)
