import os

from UAVAUTO_VERSION_4.config import db
from UAVAUTO_VERSION_4.Model.User import User
from UAVAUTO_VERSION_4.Model.Admin import Admin
from UAVAUTO_VERSION_4.Model.Operator import Operator
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

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
    def insert_operator(data, image):
        user = UserController.insert_user(data)
        fileName = str(user.id) + '_' + image.filename
        pathToSaveImage = r'E:\user\abdul wahab\PythonProjects\UAVAUTO_VERSION_4\uploads\OperatorImageData'
        full_image_path = os.path.join(pathToSaveImage, fileName)
        if user:
            image.save(full_image_path)
            operator = Operator(user_id=user.id, image_path=full_image_path)
            db.session.add(operator)
            db.session.commit()
            return {"user_id": user.id, "name": user.name,"role": user.role,"email": user.email,"id": operator.id,"image_path": operator.image_path}
        return {}

    @staticmethod
    def update_operator(data, image):
        user = User.query.filter_by(id=data['user_id'], validity=1).first()
        operator = Operator.query.filter_by(user_id=data['user_id'], validity=1).first()

        if user and operator:
            user.name = data['name']
            user.email = data['email']
            user.password = generate_password_hash(data['password'])

            if image:
                secure_name = secure_filename(image.filename)
                file_name = f"{user.id}_{secure_name}"

                path_to_save_image = r'E:\user\abdul wahab\PythonProjects\UAVAUTO_VERSION_4\uploads\OperatorImageData'

                full_image_path = os.path.join(path_to_save_image, file_name)
                image.save(full_image_path)

                operator.image_path = full_image_path
                # try:
                #     image.save(full_image_path)
                #
                #     operator.image_path = full_image_path
                # except Exception as e:
                #     print(f"Error saving image: {e}")
                #     db.session.rollback()
                #     return {"error": "Failed to save operator image."}

            # Commit updates
            db.session.commit()
            return {
                'id': operator.id,
                'name': user.name,
                'email': user.email,
                'user_id': user.id,
                'image_path': operator.image_path
            }

        return {}

    @staticmethod
    def delete_operator(operator_id):
        operator = Operator.query.filter_by(id=operator_id, validity=1).first()
        user = User.query.filter_by(id=operator.user_id, validity=1).first()
        if operator and user:
            operator.validity = 0
            user.validity = 0
            db.session.commit()
            return True
        return False

    @staticmethod
    def login_admin(data):
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email, role='admin').first()
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

    @staticmethod
    def login_operator(data):
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email, role='operator').first()
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