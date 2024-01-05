from flask import request, jsonify
from app import db
from controllers import create_user_controller, list_all_user_controller


@app.route("/user/", methods=["GET", "POST"])
def list_create_user():
    if request.method == "POST": return create_user_controller()
    if request.method == "GET": return list_all_user_controller()
    else: return "Method not Allowed"