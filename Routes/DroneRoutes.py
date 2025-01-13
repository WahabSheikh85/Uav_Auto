from flask import Blueprint,jsonify,request
from UAVAUTO_VERSION_4.Controller.DroneController import DroneController

drone_routes = Blueprint('drone_routes',__name__)

@drone_routes.route('/insert_drone',methods=['POST'])
def insert_drone():
    data = request.get_json()
    drone,drone_station_mapping = DroneController.insert_drone(data)
    drone_dict = {
        "ceiling": drone.ceiling,
        "drone_image": drone.drone_image,
        "flight_duration": drone.flight_duration,
        "fps": drone.fps,
        "id": drone.id,
        "name": drone.name,
        "speed": drone.speed,
        'station_id':drone_station_mapping.station_id,
        'status':drone_station_mapping.status,
        'drone_station_mapping_id':drone_station_mapping.id
    }
    return jsonify({'success':'Data inserted Successfully','data':drone_dict})

@drone_routes.route('/get_all_drones',methods=['GET'])
def get_all_drones():
    drones = DroneController.get_all_drones()
    return jsonify(drones)

@drone_routes.route('/delete_drone/<int:id>',methods=['DELETE'])
def delete_drone(id):
    is_deleted = DroneController.delete_drone(id)
    return jsonify({'success':is_deleted})

@drone_routes.route('/update_drone',methods=['PUT'])
def update_drone():
    data = request.get_json()
    drone = DroneController.update_drone(data)
    return jsonify({'success':True,'data':drone})