from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        dashboard_source = request.form.get('dashboard_source')
        config = request.form.get('config')
        destination_name = request.form.get('destination_name')

        # Send to Manyas Function

    return render_template("home.html")
