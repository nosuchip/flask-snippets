# -*- coding: utf-8 -*-

from flask import Flask

import filters
import json_enc


def init(name):
    app = Flask(name)

    configure_app(app)

    return app


def configure_app(app):
    app.config.from_object('config.flask_settings')


    # Define new Jinja2 tag:
    # Before: `{{ url_for('static', filename='images/logo.png') }}`
    # After: `{{ url_for_static('images/logo.png') }}`
    app.jinja_env.globals['url_for_static'] = filters.url_for_static

    # Define useful filters
    app.jinja_env.filters['app_settings_item'] = filters.app_settings_item
    app.jinja_env.filters['to_json'] = filters.to_json
    app.jinja_env.filters['percents'] = filters.percents
    app.jinja_env.filters['currency'] = filters.currency
    app.jinja_env.filters['count'] = filters.count
    app.jinja_env.filters['date'] = filters.as_date

    app.json_encoder = json_enc.ExtendedJSONEncoder


app = init(__name__)
