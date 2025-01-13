from UAVAUTO_VERSION_4.config import db
from UAVAUTO_VERSION_4.Model.User import User
from UAVAUTO_VERSION_4.Model.Admin import Admin
from UAVAUTO_VERSION_4.Model.Operator import Operator
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash


# from flask_bcrypt import Bcrypt
class UserController():
    @staticmethod
    def insert_user(data):
        user = User.query.filter_by(email=data['email'],validity=1).first()
        if not user:
            print('1')
            hashed_password = generate_password_hash(data['password'])
            user = User(name=data['name'], password=hashed_password, role=data['role'], email=data['email'])
            db.session.add(user)
            db.session.commit()
            return user
        return {}

    @staticmethod
    def insert_admin(data):
        user = UserController.insert_user(data)
        if user:
            admin = Admin(user_id=user.id, gender=data['gender'], age=data['age'], phone_no=data['phone_no'])
            db.session.add(admin)
            db.session.commit()
            return {
                "user_id": user.id,
                "name": user.name,
                "password": user.password,
                "role": user.role,
                "email": user.email,
                "admin_id": admin.id,
                "age": admin.age,
                "gender": admin.gender,
                "phone_no": admin.phone_no
            }
        return {}


    @staticmethod
    def insert_operator(data):
        user = UserController.insert_user(data)
        if user:
            operator = Operator(user_id=user.id, image_path=data['image_path'])
            db.session.add(operator)
            db.session.commit()
            return {"user_id": user.id, "name": user.name,"role": user.role,"email": user.email,"id": operator.id,"image_path": operator.image_path}
        return {}


    @staticmethod
    def update_operator(data):
        user = User.query.filter_by(id=data.get('user_id'), validity=1)
        operator = Operator.query.filter_by(user_id=data.get('user_id'), validity=1)
        if operator:
            operator.image_path = data.get('image_path', operator.image_path)
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            user.password = generate_password_hash(data.get('password', user.password))
            db.session.commit()
            return {'id': operator.id, 'name': user.name, 'email': user.email, 'user_id': user.id,
                    'image_path': operator.image_path}
        return {}

    @staticmethod
    def delete_operator(operator_id):
        operator = Operator.query.filter_by(id=operator_id, validity=1).first()
        user = User.query.filter_by(id=operator.user_id, validity=1).first()
        if operator & user:
            operator.validity = 0
            user.validity = 0
            db.session.commit()
            return True
        return False

    @staticmethod
    def login_user(data):
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user is not None:
            print("user password", user.password)
            print("password", password)
            print("is valid", check_password_hash(user.password, password))
            if check_password_hash(user.password, password):
                return True
            else:
                return False
        else:
            return False