from app import app

def test_home_returns_message():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "Hola desde Docker + GitHub Actions!"
