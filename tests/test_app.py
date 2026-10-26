from app.main import app


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.json["service"] == "cndp-advanced"


def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_readiness():
    response = app.test_client().get("/ready")
    assert response.status_code == 200
    assert response.json["status"] == "ready"


def test_info():
    response = app.test_client().get("/info")
    assert response.status_code == 200
    assert response.json["version"] == "1.0.0"


def test_not_found():
    response = app.test_client().get("/does-not-exist")
    assert response.status_code == 404
    assert response.json["error"] == "Not found"
