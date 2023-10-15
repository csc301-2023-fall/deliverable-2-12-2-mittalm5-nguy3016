from flask import Flask


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = "AzsdkqjwheqjeaposdApqEpdasb"

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
