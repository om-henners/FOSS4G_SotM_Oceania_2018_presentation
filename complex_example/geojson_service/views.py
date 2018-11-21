from datetime import datetime

from flask import Blueprint, Response, url_for, render_template, current_app


base_pages = Blueprint('base_pages', __name__)


@base_pages.route('/heartbeat')
def heartbeat():
    return Response(datetime.now().isoformat(), mimetype='text/plain')


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@base_pages.route("/")
def site_map():
    links = []
    for rule in current_app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append((url, rule.endpoint))
    # links is now a list of url, endpoint tuples
    return Response(render_template(
        'output.csv',
        rows=links,
        fieldnames=['url', 'endpoint']),
        mimetype='text/plain'
    )