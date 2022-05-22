import pytest
from django.contrib.auth.models import Group
from django.utils.datetime_safe import datetime

from authentication.models import User


@pytest.fixture
@pytest.mark.django_db
def hr_token(client, django_user_model):
    username = "Hr_test"
    password = "123qwe"
    email = "hr_test@test.ru"
    birth_date = datetime.now()
    is_active = True

    user = django_user_model
    user.objects.create_user(
        username=username,
        password=password,
        email=email,
        birth_date=birth_date,
        is_active=is_active,
        is_staff=is_active,
    )
    response = client.post(
        "/users/token/",
        {
            "username": username,
            "email": email,
            "birth_date": birth_date,
            "password": password
        },
        format="json"
    )

    return response.data["access"]

