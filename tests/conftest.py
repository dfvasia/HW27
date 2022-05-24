
from django.conf import settings
import pytest
from pytest_factoryboy import register

from tests.factories import AdsFactory, UserFactory, CharacteristicsFactory

pytest_plugins = "tests.fixtures"
DEFAULT_ENGINE = 'django.db.backends.postgresql_psycopg2'


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }


register(AdsFactory)
register(UserFactory)
register(CharacteristicsFactory)

