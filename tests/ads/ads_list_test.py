import pytest
from django import db
from django.db import connection

from ads.models import Advertisement

@pytest.mark.django_db
def test_ads_list(client):
    ads = Advertisement.objects.create(
        name="123",
        author_id=5,
        price=2500,
        description="321",
        category_id=4,
        is_published=False,
    )
    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
                "id": ads.pk,
                "name": "123",
                "is_published": False,
                "price": 2500,
                "description": "321",
                "image": None,
                "author": 5,
                "category": 4
        }]
    }
    response = client.get("/ad/")

    assert response.status_code == 200
    assert response.data == expected_response



