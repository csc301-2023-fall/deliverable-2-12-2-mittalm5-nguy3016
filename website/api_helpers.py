import requests

from website.endpoints import DASHBOARD_ENDPOINT, CHART_ENDPOINT, DATASET_ENDPOINT
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
    dashboards = requests.get(SUPERSET_INSTANCE_URL + DASHBOARD_ENDPOINT, headers=headers).json()

    dashboard_names = []
    for dashboard in dashboards["result"]:
        dashboard_names.append((dashboard["id"], dashboard["dashboard_title"]))
    return dashboard_names


def get_charts(token, dashboard_id):
    headers = {"Authorization": "Bearer " + token}
    charts = requests.get(SUPERSET_INSTANCE_URL + DASHBOARD_ENDPOINT + str(dashboard_id) + '/charts', headers=headers).json()
    chart_names = []
    for chart in charts["result"]:
        chart_names.append(chart["slice_name"])
    return chart_names


def get_datasets(token):
    headers = {"Authorization": "Bearer " + token}
    datasets = requests.get(SUPERSET_INSTANCE_URL + DATASET_ENDPOINT, headers=headers).json()
    dataset_names = []
    for dataset in datasets["result"]:
        dataset_names.append(dataset["table_name"])
    return dataset_names
