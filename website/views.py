from flask import Blueprint, render_template, request
from website.pocFiles.endpoints import DASHBOARD_ENDPOINT
from website.pocFiles.superset_constants import (
    SUPERSET_INSTANCE_URL,
    SUPERSET_USERNAME,
    SUPERSET_PASSWORD
)
import requests
import os

views = Blueprint('views', __name__)


@views.route('/')
def home():

    login_data = {
        "username": SUPERSET_USERNAME,
        "password": SUPERSET_PASSWORD,
        "provider": "db"
    }

    # makes a post request to get access token
    token = requests.post(SUPERSET_INSTANCE_URL + "/api/v1/security/login", json=login_data).json()["access_token"]

    # using the token to get all the dashboards
    headers = {"Authorization": "Bearer " + token}
    dashboards = requests.get(SUPERSET_INSTANCE_URL + DASHBOARD_ENDPOINT, headers=headers).json()

    # passing in the dashboard titles to the html file to output them
    html_data = {}
    for result in dashboards["result"]:
        html_data[result["id"]] = result["dashboard_title"]
    return render_template("home.html", data=html_data)


@views.route('/clone', methods=['POST'])
def clone():
    # dashboard_source = request.form.get('dashboard_source')
    # config = request.form.get('config')
    # destination_name = request.form.get('destination_name')

    # simulating a call to a command line command
    os.system('python website/export_dashboard.py -d "[ untitled dashboard ]" -o "test.json"')

    return "Form Submitted"


