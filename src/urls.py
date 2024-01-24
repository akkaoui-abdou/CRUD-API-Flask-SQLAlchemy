from flask import request, jsonify, Blueprint
from src.controllers import (register_user_controller,
    login_user_controller, 
    protected_user_controller, 
    create_user_controller, 
    list_all_user_controller, 
    retrieve_user_controller,
    update_user_controller,
    delete_user_controller
    )
from flask_jwt_extended import jwt_required, get_jwt_identity

bp_user = Blueprint('user', __name__)
@bp_user.route("/user", methods=["GET", "POST"])
def list_create_user():
    if request.method == "POST": return create_user_controller()
    if request.method == "GET": return list_all_user_controller()
    else: return "Method not Allowed"

@bp_user.route('/register', methods=['POST'])
def register_user():
    if request.method == "POST": return register_user_controller()


@bp_user.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def maj_user(user_id):
    if request.method == "PUT": return update_user_controller(user_id)
    if request.method == "DELETE": return delete_user_controller(user_id)
    if request.method == "GET": return retrieve_user_controller(user_id)


@bp_user.route('/login', methods=['POST'])
def login_user():
    if request.method == "POST": return login_user_controller()


@bp_user.route('/protected', methods=['GET'])
@jwt_required()
def protected_user():
    if request.method == "GET": return protected_user_controller()    