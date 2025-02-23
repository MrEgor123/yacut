from random import choices as choice
from string import ascii_letters, digits
from sqlalchemy.sql import exists

from .models import URLMap


def get_unique_short_id(list=ascii_letters + digits, k=6):
    while True:
        short_id = ''.join(choice(list, k=k))
        if not URLMap.query.session.query(
                exists().where(URLMap.short == short_id)
        ).scalar():
            return short_id