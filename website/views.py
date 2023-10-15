from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():

    data = {
        'id1': 'Dashboard 1',
        'id2': 'Dashboard 2',
        'id3': 'Dashboard 3',
        'id4': 'Dashboard 4'
    }

    return render_template("home.html", data=data)


@views.route('/clone', methods=['POST'])
def clone():
    # Send to Manyas Function
    dashboard_source = request.form.get('dashboard_source')
    config = request.form.get('config')
    destination_name = request.form.get('destination_name')

    return render_template("clone.html")
