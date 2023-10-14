import json

from flask import Blueprint, render_template, request
from website.pocFiles.api_request_handler import APIRequestHandler
from website.pocFiles.export_dashboard import export_dashboard, _get_dashboard_id
from website.pocFiles.endpoints import DASHBOARD_ENDPOINT, DATASET_ENDPOINT
from website.pocFiles.superset_constants import (
    SUPERSET_INSTANCE_URL,
    SUPERSET_USERNAME,
    SUPERSET_PASSWORD
)

views = Blueprint('views', __name__)


@views.route('/')
def home():
    # we can make a get request to get a list of all the dashboards and display it, instead of just the text field

    # request_handler = APIRequestHandler(SUPERSET_INSTANCE_URL, SUPERSET_USERNAME, SUPERSET_PASSWORD)
    # dashboard_get_response = request_handler.get_request(DASHBOARD_ENDPOINT)
    # dashboards = json.loads(dashboard_get_response.text)['result']
    # print(dashboards)
    return render_template("home.html")


@views.route('/clone', methods=['POST'])
def clone():
    dashboard_source = request.form.get('dashboard_source')
    config = request.form.get('config')
    destination_name = request.form.get('destination_name')

    # call extract_dashboards here
    return "Form Submitted"
