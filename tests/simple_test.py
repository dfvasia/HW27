def test_a():
    assert True


def test_major_page(client):
    response = client.get("/")

    assert response.status_code == 200
