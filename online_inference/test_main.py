import json
import pytest
from fastapi.testclient import TestClient
from main_online_inference import app, load_model

def main():
    global client
    client = TestClient(app)

main()

@pytest.fixture(scope='session', autouse=True)
def test_model_initialization():
    load_model()


def test_endpoints_predict_disease():
    request = {
        "age": 59,
        "sex": 1,
        "cp": 0,
        "trestbps": 170,
        "chol": 288,
        "fbs": 0,
        "restecg": 2,
        "thalach": 159,
        "exang": 0,
        "oldpeak": 0.2,
        "slope": 1,
        "ca": 0,
        "thal": 2,
    }

    response = client.post(
        '/predict',
        json.dumps(request)
    )

    assert response.status_code == 200
    assert response.json() == {'condition': 'disease'}


def test_endpoints_predict_no_disease():
    request = {
        "age": 69,
        "sex": 0,
        "cp": 0,
        "trestbps": 160,
        "chol": 234,
        "fbs": 1,
        "restecg": 2,
        "thalach": 131,
        "exang": 0,
        "oldpeak": 0.1,
        "slope": 1,
        "ca": 1,
        "thal": 0,
    }

    response = client.post(
        '/predict',
        json.dumps(request)
    )

    assert response.status_code == 200
    assert response.json() == {'condition': 'no disease'}


def test_endpoints_health():
    response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == 'Model is ready'


def test_skipped_fields():
    request = {
        "age": 69,
        "sex": 1,
        "cp": 0,
        "trestbps": 160,
        "chol": 234,
        "fbs": 1,
        "restecg": 2,
        "exang": 0,
        "oldpeak": 0.1,
        "slope": 1,
        "ca": 1,
        "thal": 0,
    }

    response = client.post(
        '/predict',
        json.dumps(request)
    )

    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'field required'


def test_fields_numerical():
    request = {
        "age": 50,
        "sex": 1,
        "cp": 0,
        "trestbps": 1000,
        "chol": 234,
        "fbs": 1,
        "restecg": 2,
        "thalach": 131,
        "exang": 0,
        "oldpeak": 0.1,
        "slope": 1,
        "ca": 1,
        "thal": 0,
    }

    response = client.post(
        '/predict',
        json.dumps(request)
    )

    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'Wrong trestbps value'


def test_fields_categorical():
    request = {
        "age": 69,
        "sex": 1,
        "cp": 0,
        "trestbps": 160,
        "chol": 234,
        "fbs": 1,
        "restecg": 2,
        "thalach": 131,
        "exang": 0,
        "oldpeak": 0.1,
        "slope": 1,
        "ca": 1,
        "thal": 131,
    }

    response = client.post(
        '/predict',
        json.dumps(request)
    )
    
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'unexpected value; permitted: 0, 1, 2'
