

# sadece production ile ilgili olan kodlari buraya alip base.py dan siliyoruz.
## dev de baska prod da baska db kullan. 

from .base import *


DATABASES = {"default": {"ENGINE": "django.db.backends.postgresql_psycopg2", "NAME": config("SQL_DATABASE"), "USER": config(
    "SQL_USER"), "PASSWORD": config("SQL_PASSWORD"), "HOST": config("SQL_HOST"), "PORT": config("SQL_PORT"), "ATOMIC_REQUESTS": True}}
