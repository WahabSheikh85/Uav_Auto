from UAVAUTO_VERSION_4.Model.MissionTask import MissionTask
from UAVAUTO_VERSION_4.Model.MissionPlanner import MissionPlanner
from UAVAUTO_VERSION_4.config import db

class MissionTaskController():
    @staticmethod
    def insert_mission_task(data):
        mission_planner = MissionPlanner.query.filter_by(id=data['mission_planner_id']).first()
        mission_task = MissionTask(mission_planner_id=data['mission_planner_id'],description=data['description'])
        db.session.add(mission_task)
        db.session.commit()
        mission_planner.status = 'active'
        db.session.commit()
        return mission_task

    @staticmethod
    def change_mission_status(data):
        mission_planner = MissionPlanner.query.filter_by(id=data.get('mission_planner_id')).first()
        if mission_planner:
            mission_planner.status = data.get('status')
            db.session.commit()
            return True
        return False