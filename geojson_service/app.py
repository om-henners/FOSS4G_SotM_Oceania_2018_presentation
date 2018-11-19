from flask import Flask

from .views import base_pages


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('GEOJSON_SERVER_SETTINGS')
    app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.png'))

    @app.after_request
    def gnu_terry_pratchett(resp):
        resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
        return resp

    app.register_blueprint(base_pages)

    return app
