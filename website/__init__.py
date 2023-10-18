from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')

    from .views import views
    from .export_dashboard import export_dashboard

    app.register_blueprint(views, url_prefix='/')

    return app
