import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import init_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    init_db()

def test_create_and_search_patient():
    payload = {
        "full_name": "Test Patient",
        "date_of_birth": "2020-01-01",
        "sex": "M",
        "region": "Center",
        "district": "Douala",
        "contact": "+237600000000"
    }
    res = client.post('/patients', json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data['nhi'].startswith('NHI-')

    # search by name
    res2 = client.get('/patients', params={'q': 'Test Patient'})
    assert res2.status_code == 200
    arr = res2.json()
    assert len(arr) >= 1

    # duplicate attempt
    res3 = client.post('/patients', json=payload)
    assert res3.status_code == 400
