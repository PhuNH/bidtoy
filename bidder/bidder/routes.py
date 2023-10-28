from flask import request

from . import app, db
from .models import Impression


@app.route('/')
def index():
    return 'Welcome to bidder'


def calc_bid(imp_profile: str) -> int:
    bidder_profile = app.config['PROFILE']
    print(f"Bidder: '{bidder_profile}'; Impression: '{imp_profile}'")

    bid = 0
    for idx in range(20):
        # Only compare each valid (i.e. non-space) attribute of bidder with the
        #   respective one of impression
        if (b := bidder_profile[idx]) != ' ':
            i = imp_profile[idx]
            diff = abs(ord(i) - ord(b))
            # Consider the attribute compatible when the difference is smaller
            #   than 3
            if diff < 3:
                # The "partial bid" of a compatible attribute is `5 - diff`
                #   which is in range(3, 6) (diff is in range(3)).
                # The bid for the impression is 5 times the sum of partial
                #   bids of all compatible attributes.
                bid += 5 * (5 - diff)
    # When there's no compatible attribute, no bid is made
    return bid


@app.route('/new-imp', methods=['POST'])
def receive_imp():
    imp_profile = request.data.decode('ascii')
    bid = calc_bid(imp_profile)
    print(f'Bid: {bid}')
    # db.session.add(Impression(profile=imp_profile, bid=bid))
    return str(bid)
