from flask import Blueprint,jsonify,request
from UAVAUTO_VERSION_4.Controller.MissionPlannerController import MissionPlannerController

mission_planner_routes = Blueprint('mission_planner_routes',__name__)

@mission_planner_routes.route('/insert_mission_plan',methods=['POST'])
def insert_mission_plan():
    data = request.get_json()
    mission_plan = MissionPlannerController.insert_mission_plan(data)

    return jsonify({"success":True,'data':mission_plan}),200

@mission_planner_routes.route('/update_mission_plan',methods=['PUT'])
def update_mission_plan():
    data = request.get_json()
    is_updated = MissionPlannerController.update_mission_plan(data)
    if is_updated:
        return jsonify({'success':True}),200
    else:
        return jsonify({'success':False}),400

@mission_planner_routes.route('/delete_mission_plan/<int:id>',methods=['DELETE'])
def delete_mission_plan(id):
    is_deleted = MissionPlannerController.delete_mission_plan(id)
    if is_deleted:
        return jsonify({'success':True}),200
    else:
        return jsonify({'success':False}),400

@mission_planner_routes.route('/get_history',methods=['GET'])
def get_history():
    mission_plan = MissionPlannerController.get_history()
    return jsonify({'success':True,'data':mission_plan}),200
