import pytest


@pytest.mark.django_db
def test_retrieve_vacancy(client, advertisement, hr_token):
    expected_response = {
        "id": advertisement.pk,
        "name": "test_test_test_",
        "author": advertisement.author_id,
        "price": 2500,
        "description": "test_test",
        "is_published": False,
        "category": advertisement.category,
        "image": None,
    }

    response = client.get(
        f"/vacancy/{advertisement.pk}/",
        HTTP_AUTHORIZATION="Bearer %s" % hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
