import click
import json
import random
import string
import yaml

# from .api_request_handler import APIRequestHandler
# from .api_request_handler import APIRequestHandler
from website.endpoints import DASHBOARD_ENDPOINT
from website.superset_constants import (
    SUPERSET_INSTANCE_URL,
    SUPERSET_USERNAME,
    SUPERSET_PASSWORD
)
from website.api_request_handler import APIRequestHandler


def _get_random_string(size=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


@click.command()
@click.option(
    "-d",
    "--dashboard_title",
    required=True,
    type=str,
    help="Name of dashboard to be exported",
)
@click.option(
    "-o",
    "--output_file",
    default=f"dashboard_{_get_random_string()}.json",
    type=str,
    help="Name of output file, defaults to dashboard_<random_string>.json",
)
def export_dashboard(dashboard_title, output_file):
    print("reached")
    print(SUPERSET_INSTANCE_URL)
    request_handler = APIRequestHandler(SUPERSET_INSTANCE_URL, SUPERSET_USERNAME, SUPERSET_PASSWORD)
    dashboard_id = _get_dashboard_id(dashboard_title, request_handler)

    if dashboard_id >= 0:
        endpoint = f"{DASHBOARD_ENDPOINT}export/?q=[{dashboard_id}]"
        export_request = request_handler.get_request(endpoint)
        # print(json.loads(export_request.text))

        extracted_data = extract_between_markers(export_request.text)

        attributes_dict = yaml.safe_load(extracted_data)
        yaml_output = yaml.dump(attributes_dict)
        with open('data.yml', 'w') as f:
            f.write(yaml_output)

        with open('data.yml', 'r') as file:
            data = yaml.safe_load(file)

        final_data = {
            "dashboards": [
                {
                    "__Dashboard__": data
                }
            ]
        }

        with open('test.json', 'w') as json_file:
            json.dump(final_data, json_file)

        print(f"Dashboard details of '{dashboard_title}' written to {output_file}")
    else:
        print(f"Error: No dashboard with title '{dashboard_title}' found.")


def _get_dashboard_id(dashboard_title, request_handler):
    dashboard_request = request_handler.get_request(DASHBOARD_ENDPOINT)
    resp_dashboard = dashboard_request.json()

    for result in resp_dashboard["result"]:
        if result["dashboard_title"].lower() == dashboard_title.lower():
            return result["id"]

    return -1


def extract_between_markers(data):
    start_marker = "dashboard_title:"
    end_marker = "version:"

    metadata_index = data.find("metadata")
    data = data[:metadata_index] + "json_metadata" + data[metadata_index + 8:]
    position_index = data.find("position")
    data = data[:position_index] + "position_json" + data[position_index + 8:]

    start_index = data.find(start_marker)
    end_index = data.find(end_marker, start_index)

    if start_index != -1 and end_index != -1:
        return data[start_index:end_index + len(end_marker) + 6]
    else:
        return None


def get_json_object(filepath):
    with open('test.json', 'r') as f:
        data = json.load(f)
        return data


def save_to_yaml(data, output_file):
    with open(output_file, 'w') as f:
        yaml.dump(data, f)


def _write_to_file(dashboard_json, output_file):
    with open(output_file, 'w') as dashboard_file:
        json.dump(dashboard_json, dashboard_file, indent=4)


if __name__ == "__main__":
    export_dashboard()
