from flask import Flask

from .views import base_pages
from .voting_centre_views import vc_pages


def create_app():
    app = Flask(__name__)
    app.config.from_envvar('GEOJSON_SERVER_SETTINGS')
    app.add_url_rule('/favicon.ico', 'favicon', lambda: app.send_static_file('favicon.png'))

    @app.after_request
    def gnu_terry_pratchett(resp):
        resp.headers.add("X-Clacks-Overhead", "GNU Terry Pratchett")
        return resp

    from .models import db
    db.init_app(app)

    from .serializer_utils import ma
    ma.init_app(app)

    app.register_blueprint(base_pages)
    app.register_blueprint(vc_pages, url_prefix='/centres')

    return app
