from flask import Blueprint,request,jsonify
from UAVAUTO_VERSION_4.Controller.RoutesController import RoutesController

routes_controller_routes = Blueprint('routes_controller_routes',__name__)

@routes_controller_routes.route('/insert_route',methods=['POST'])
def insert_route():
    data = request.get_json()
    routes = RoutesController.insert_route(data)
    return jsonify({'success':True,'data':routes})

@routes_controller_routes.route('/get_routes',methods=['GET'])
def get_routes():
    routes = RoutesController.get_routes()
    if routes:
        return jsonify({'success':True,'data':routes})
    else:
        return jsonify({'success':False,'data':routes})
