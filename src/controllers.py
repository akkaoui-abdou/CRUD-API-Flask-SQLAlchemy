from flask import request, jsonify
from models import db, User  # Import the db instance and models
import uuid
#from app import db


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
    request_form = request.form.to_dict()
    user = User.query.get(user_id)

    user.email        = request_form['email']
    user.username     = request_form['username']
    user.dob          = request_form['dob']
    user.country      = request_form['country']
    user.phone_number = request_form['phone_number']
    db.session.commit()

    response = User.query.get(user_id).toDict()
    return jsonify(response)

def delete_user_controller(user_id):

    User.query.filter_by(id=user_id).delete()
    db.session.commit()

    return ('Account with Id "{}" deleted successfully!').format(user_id)