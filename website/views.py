from flask import Blueprint, render_template
import os
from website.api_helpers import get_access_token, get_dashboards

views = Blueprint('views', __name__)


@views.route('/')
def home():

    token = get_access_token()
    dashboards = get_dashboards(token)

    # passing in the dashboard titles to the html file to output them
    html_data = {}
    for result in dashboards["result"]:
        html_data[result["id"]] = result["dashboard_title"]
    return render_template("home.html", data=html_data)


@views.route('/clone', methods=['POST'])
def clone():

    # simulating a call to a command line command
    os.system('python website/export_dashboard.py -d "test" -o "test.json"')
    os.system('python website/create_derived_dashboard.py -f test.json '
              '-c website/test_config_map.json -n test_copy')

    return render_template("clone.html")


