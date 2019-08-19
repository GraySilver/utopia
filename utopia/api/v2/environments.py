from flask import Blueprint, jsonify

from core import Utopia
from decorators import is_user_logged_in

environments = Blueprint("environments", __name__)
utopia = Utopia.getInstance()


@environments.route("/")
@is_user_logged_in()
def get_environments():
    return jsonify(status="success", environments=utopia.serialize_environments())
