from flask import request, jsonify
from src.models import db, User  # Import the db instance and models
import uuid
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

def register_user_controller():
    data = request.get_json()
    new_user = User(username=data['username'], password=data['password'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='User created successfully'), 201


def login_user_controller():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()

    if user and user.password == data['password']:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401


def protected_user_controller():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


def create_user_controller():
    request_form = request.form.to_dict()

    id = str(uuid.uuid4())

    new_user = User(
        id       = id,
        username = request_form["username"],
        email    = request_form["email"],
    )
    db.session.add(new_user)
    db.session.commit()

    response = User.query.get(id).toDict()
    return jsonify(response)

def list_all_user_controller():

    users = User.query.all()

    listUser = []

    for user in users:
        listUser.append(user.toDict())

    return jsonify(listUser)    

def retrieve_user_controller(user_id):
    response = User.query.get(user_id).toDict()
    return jsonify(response)



def update_user_controller(user_id):
    #request_form = request.form.to_dict()
    request_form = request.get_json()
    
    user = User.query.get(user_id)

    user.email        = request_form['email']
    #user.username     = request_form['username']
    #user.password     = request_form['password']
    user.role      = request_form['role']
    db.session.commit()

    response = User.query.get(user_id).toDict()
    return jsonify(response)

def delete_user_controller(user_id):

    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return ('Account with Id "{}" deleted successfully!').format(user_id)