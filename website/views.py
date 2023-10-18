import os
from flask import Blueprint, render_template, request, jsonify
from website.api_helpers import get_access_token, get_dashboards, get_charts, get_datasets

views = Blueprint('views', __name__)


@views.route('/')
def index():
    html_data = get_dataset_to_chart_mapping()
    return render_template("index.html", html_data=html_data)


def get_dataset_to_chart_mapping():
    token = get_access_token()
    dashboards = get_dashboards(token)
    datasets = get_datasets(token)

    dataset_to_chart_map = {}
    all_charts = []
    for d1, d1Name in dashboards:
        charts = get_charts(token, d1)
        all_charts.append(charts)

        dataset_to_chart_map[d1] = {
            "charts": charts,
            "datasets": datasets
        }

    html_data = {
        "dashboards": dashboards,
        "charts": all_charts,
        "datasets": datasets,
        "datasetChartMapping": dataset_to_chart_map
    }
    return html_data


@views.route('/clone', methods=['POST'])
def clone():
    dashboard_source = request.form.get('dashboard_source')
    destination_name = request.form.get('destination_name')

    chart_names = []
    chart_tables = []

    index = 0
    while True:
        chart_name = request.form.get(f'chart{index}')
        dataset = request.form.get(f'dataset{index}')

        if chart_name is None or dataset is None:
            break

        chart_names.append(chart_name)
        chart_tables.append(dataset)
        index += 1

    # To prove it works
    print(dashboard_source)
    print(chart_names)
    print(chart_tables)
    print(destination_name)

    # To be completed after meeting with our partner
    # simulating a call to a command line command

    # os.system(f'python website/export_dashboard.py -d "{dashboard_source}" -o "{dashboard_source}.json"')
    # os.system(f'python website/create_derived_dashboard.py -f {dashboard_source}.json '
    #           f'-c website/test_config_map.json -n {destination_name}')

    return render_template("clone.html")


@views.route('/get_dataset_chart_mapping', methods=['GET'])
def get_dataset_chart_mapping():
    return jsonify(get_dataset_to_chart_mapping()["datasetChartMapping"])

