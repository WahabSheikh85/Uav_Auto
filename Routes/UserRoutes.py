from tkinter.font import names

from flask import Blueprint, jsonify, request
from UAVAUTO_VERSION_4.Controller.UserController import UserController

# Create a blueprint for user routes
user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/insert_user', methods=['POST'])
def insert_user():
    data = request.get_json()
    user = UserController.insert_user(data)
    user_dict = {
        "user_id": user.id,
        "name": user.name,
        "password": user.password,
        "role": user.role,
        "email": user.email
    }
    return jsonify({'success': 'Data inserted successfully','data':user_dict}),200

@user_routes.route('/insert_admin',methods=['POST'])
def insert_admin():
    data = request.get_json()
    admin = UserController.insert_admin(data)
    if admin:
        return jsonify({'success': True,'data':admin}),200
    return jsonify({'success': False,'data':"This user already exists"}),400

@user_routes.route('/insert_operator',methods=['POST'])
def insert_operator():
    # data = request.get_json()
    image = request.files['image']
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')
    email = request.form.get('email')
    data = {
        'name': name,
        'password': password,
        'role': role,
        'email': email
    }
    operator = UserController.insert_operator(data, image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    return jsonify({'success':False,'data':"This user already exists"}),400

@user_routes.route('/login_admin',methods=['GET'])
def login_admin():
    data = request.get_json()
    is_valid = UserController.login_admin(data)
    return {'success':is_valid}

@user_routes.route('/login_operator',methods=['GET'])
def login_operator():
    data = request.get_json()
    is_valid = UserController.login_operator(data)
    return {'success':is_valid}

@user_routes.route('/update_operator',methods=['PUT'])
def update_operator():
    # data = request.get_json()
    data = {
        'user_id': request.form.get('user_id'),
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'password': request.form.get('password')
    }
    image = request.files['image']
    operator = UserController.update_operator(data, image)
    if operator:
        return jsonify({'success':True,'data':operator}),200
    else:
        return jsonify({'success':False,'data':operator}),400

@user_routes.route('/delete_operator/<int:id>',methods=['DELETE'])
def delete_operator(id):
    isDeleted = UserController.delete_operator(id)
    return jsonify({'success':isDeleted})