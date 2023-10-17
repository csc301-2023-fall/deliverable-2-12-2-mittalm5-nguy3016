import requests

from website.endpoints import DASHBOARD_ENDPOINT
from website.superset_constants import SUPERSET_PASSWORD, SUPERSET_USERNAME, SUPERSET_INSTANCE_URL


def get_access_token():
    login_data = {
        "username": SUPERSET_USERNAME,
        "password": SUPERSET_PASSWORD,
        "provider": "db"
    }

    # makes a post request to get access token
    token = requests.post(SUPERSET_INSTANCE_URL + "/api/v1/security/login", json=login_data).json()["access_token"]
    return token


def get_dashboards(token):
    # using the token to get all the dashboards
    headers = {"Authorization": "Bearer " + token}
    return requests.get(SUPERSET_INSTANCE_URL + DASHBOARD_ENDPOINT, headers=headers).json()
