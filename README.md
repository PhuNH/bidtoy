# bidtoy

A toy program consisting of two servers:
- A bidnet suggesting impressions to be bid for
- A bidder making bids for those impressions

### Concept

- A profile is a string of lowercase letters a-z, each position in the string
stands for an attribute of the profile, the letter at a position stands for
the strength of the corresponding attribute;
- An impression has a profile of length 20;
- A bidder's profile also has length of 20, but only 5 are concerned attributes
(i.e. letters), 15 are irrelevant (i.e. spaces). The profile is used for the
bidder to decide whether an impression is worth investing in, based on the
compatibility between the impression's profile and the bidder's profile;
- A bidnet is assumed to have received impressions from publishers and now will
update the bidder with one impression for every 5 seconds, the bidder needs to
tell the bidnet how much it wants to bid for the impression, the bidnet then
confirms with the bidder whether it has won the impression. For simplicity, the
bidder will win as long as it makes a positive bid.

### Install

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
```

### How it works

- Start bidnet (address is set to `localhost:1331`)

```bash
cd bidnet
flask run
```

- Open another terminal window, start bidder (address is set to `localhost:1441`)

```bash
. .venv/bin/activate
cd bidder
flask db upgrade
flask run
```

- Open `localhost:1331/start` to start a job on bidnet;
- The bidnet job generates one impression every 5 seconds and `post`s to bidder
`/imp` about the newly generated impression;
- The bidder after receiving information about the new impression will decide
whether to bid based on its compatibility with the impression's profile, and
send its response back: 0 means it doesn't bid, and a number greater than 0
means it does bid, the number is the value of the bid. See how to calculate the
bid in `bidder/routes.py`;
- The bidnet records the bidder's response and `put`s update to the bidder
`/imp/<id>` about whether it has won the impression;
- The bidder `/` returns impressions that it has won.