from UAVAUTO_VERSION_4.config import db
from UAVAUTO_VERSION_4.Model.MissionDataLocation import MissionDataLocation

class MissionDataLocationController():
    @staticmethod
    def insert_mission_data_location(data):
        mission_data_location = MissionDataLocation(mission_task_id=data['mission_task_id'],latitude=data['latitude'],longitude=data['longitude'],damage=data['damage'])
        db.session.add(mission_data_location)
        db.session.commit()
        return {'id': mission_data_location.id,
                'mission_task_id': mission_data_location.mission_task_id,
                'latitude': mission_data_location.latitude,
                'longitude': mission_data_location.longitude,
                'damage': mission_data_location.damage}
