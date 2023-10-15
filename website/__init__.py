from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "AzsdkqjwheqjeaposdApqEpdasb"

    from .views import views
    from website import pocFiles
    from .export_dashboard import export_dashboard

    app.register_blueprint(views, url_prefix='/')

    return app
