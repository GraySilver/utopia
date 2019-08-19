#!/usr/bin/env python3
import argparse
import signal
import os
from flask import Flask, render_template, jsonify, g
from flask_sqlalchemy import SQLAlchemy

from version import __version__

db = SQLAlchemy()


def create_app(utopia):
    from api.v2 import register_blueprints

    app = Flask(
        __name__,
        static_folder="ui/build",
        static_url_path="",
        template_folder="ui/build",
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = utopia.database
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = os.urandom(24)

    db.init_app(app)

    app.add_url_rule("/", "index", lambda: render_template("index.html"))
    app.add_url_rule(
        "/api/version",
        "version",
        lambda: jsonify(status="success", version=__version__),
    )

    @app.errorhandler(404)
    @app.errorhandler(400)
    def _(error):
        return jsonify(status="error", message=error.description), error.code

    register_blueprints(app)

    return app


def configure(config_file_path):
    from core import Utopia
    from loggers import ActivityLog
    from controllers import check_database

    utopia = Utopia(config_file_path=config_file_path)
    _ = ActivityLog(log_path=utopia.activity_log)

    app = create_app(utopia)

    # Check database
    with app.app_context():
        check_database()

    signal.signal(signal.SIGHUP, lambda signum, frame: utopia.reload())

    return app, utopia


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Utopia server")

    parser.add_argument(
        "-c", "--config-file", "--config", help="config file", required=True
    )
    parser.add_argument("--host", help="Host of the utopia", default="0.0.0.0")
    parser.add_argument("-p", "--port", help="Port of the utopia", default="5000")
    parser.add_argument(
        "--debug", help="Debug mode of the utopia", action="store_true"
    )
    parser.add_argument(
        "--auto-reload",
        help="Reload if app code changes (dev mode)",
        action="store_true",
    )
    parser.add_argument("--version", action="version", version=__version__)

    args = parser.parse_args()
    app, utopia = configure(args.config_file)

    app.run(
        host=args.host, port=args.port, use_reloader=args.auto_reload, debug=args.debug,threaded =True
    )
