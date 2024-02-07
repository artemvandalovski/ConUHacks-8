import pytest, json

DATE = "2022-10-01"


@pytest.fixture
def app():
    from app.routes import app

    app.config.update(
        {
            "TESTING": True,
        }
    )

    with app.test_client() as client:
        yield client


def test_get_schedule(app):
    response = app.get(f"/schedule/{DATE}")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["date"] == DATE
