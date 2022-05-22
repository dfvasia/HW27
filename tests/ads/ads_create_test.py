import pytest


@pytest.mark.django_db
def test_create_ads(client, hr_token):
    expected_response = {
        "id": 103,
        "name": "test_test_test_",
        "author": 12,
        "price": 2500,
        "description": "test_test",
        "is_published": False,
        "category": 3,
        "image": None,
    }
    data = {
        "name": "test_test_test_",
        "author": 12,
        "price": 2500,
        "description": "test_test",
        "category": 3,
        "is_published": False
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Bearer %s" % hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response
