import requests

from website.endpoints import DASHBOARD_ENDPOINT, DATASET_ENDPOINT
from website.superset_constants import SUPERSET_PASSWORD, SUPERSET_USERNAME, SUPERSET_INSTANCE_URL
from website.api_helpers import get_access_token


def test_access_token():
    login_data = {
        "username": SUPERSET_USERNAME,
        "password": SUPERSET_PASSWORD,
        "provider": "db"
    }

    # makes a post request to get access token
    response = requests.post(SUPERSET_INSTANCE_URL + "/api/v1/security/login", json=login_data)

    assert response.status_code == 200
    assert response.json()["access_token"] is not None


def test_get_dashboards():

    token = get_access_token()
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(SUPERSET_INSTANCE_URL + DASHBOARD_ENDPOINT, headers=headers)

    assert response.status_code == 200
    assert response.json()["result"] is not None


def test_get_datasets():

    token = get_access_token()
    headers = {"Authorization": "Bearer " + token}
    response = requests.get(SUPERSET_INSTANCE_URL + DATASET_ENDPOINT, headers=headers)

    assert response.status_code == 200
    assert response.json()["result"] is not None


# add more tests later
