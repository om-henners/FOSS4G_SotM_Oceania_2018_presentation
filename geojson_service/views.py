from datetime import datetime

from flask import Blueprint, Response


base_pages = Blueprint('base_pages', __name__)


@base_pages.route('/heartbeat')
def heartbeat():
    return Response(datetime.now().isoformat(), mimetype='text/plain')
