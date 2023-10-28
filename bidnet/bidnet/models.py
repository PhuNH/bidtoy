import random
import string
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Impression:
    profile: str = ''
    created_at: datetime = field(default_factory=datetime.utcnow)

    @classmethod
    def profile_generator(cls):
        profile = ''.join([random.choice(string.ascii_lowercase) for _ in range(20)])
        return profile

    def __post_init__(self):
        self.profile = self.profile_generator()

    def __repr__(self):
        return f'Impression with profile {self.profile} created at {self.created_at}'
