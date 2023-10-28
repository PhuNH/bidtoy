import os
import random
import string

basedir = os.path.abspath(os.path.dirname(__file__))


def profile_generator(length=5):
    profile = [random.choice(string.ascii_lowercase) for _ in range(length)]
    profile.extend(' ' * (20-length))
    random.shuffle(profile)
    profile = ''.join(profile)
    return profile


class Config:
    SQLALCHEMY_DATABASE_URI = (os.environ.get('DATABASE_URL') or
                               'sqlite:///' + os.path.join(basedir, 'bidder.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SCHEDULER_API_ENABLED = True

    PROFILE = profile_generator()

    BIDNET_ADDR = "http://127.0.0.1:1331/"
