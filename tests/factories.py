import factory.django
from django.utils.datetime_safe import datetime

from ads.models import Advertisement, Characteristics
from authentication.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "Hr_test"
    password = "123qwe"
    email = "hr_test@test.ru"
    birth_date = datetime.now()
    is_active = True


class CharacteristicsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Characteristics

    name = "CHAR_test2222"
    slug = "CHARac"


class AdsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    name = "test_test_test_"
    author = factory.SubFactory(UserFactory)
    price = 2500
    description = "test_test"
    category = factory.SubFactory(CharacteristicsFactory)
    is_published = False
