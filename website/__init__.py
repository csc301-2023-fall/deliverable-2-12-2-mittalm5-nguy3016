from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "AzsdkqjwheqjeaposdApqEpdasb"

    from .views import views
    from website import pocFiles

    app.register_blueprint(views, url_prefix='/')

    return app
