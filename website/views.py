from flask import Blueprint, render_template, request, jsonify

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def index():
    # Fake example data to be changed
    dashboards = [(1, "dashboard1"), (2, "dashboard2"), (3, "dashboard3")]
    charts = [(1, "d1slice1"), (1, "d1slice2"), (1, "d1slice3"), (2, "d2slice1"), (2, "d2slice2"), (3, "d3slice1")]
    datasets = ["table1", "table2", "table3", "table4", "table5", "table6"]
    datasetChartMapping = {
        1: {
            "charts": ["d1slice1", "d1slice2", "d1slice3"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"]
        },
        2: {
            "charts": ["d2slice1", "d2slice2"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"]
        },
        3: {
            "charts": ["d3slice1"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"]
        }
    }

    html_data = {
        "dashboards": dashboards,
        "charts": charts,
        "datasets": datasets,
        "datasetChartMapping": datasetChartMapping
    }

    return render_template("index.html", html_data=html_data)


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

    # Send to Manyas Function
    # To be completed after meeting with our partner

    return render_template("clone.html")


@views.route('/get_dataset_chart_mapping', methods=['GET'])
def get_dataset_chart_mapping():
    datasetChartMapping = {
        1: {
            "charts": ["d1slice1", "d1slice2", "d1slice3"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"],
        },
        2: {
            "charts": ["d2slice1", "d2slice2"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"],
        },
        3: {
            "charts": ["d3slice1"],
            "datasets": ["table1", "table2", "table3", "table4", "table5", "table6"],
        },
    }

    return jsonify(datasetChartMapping)
