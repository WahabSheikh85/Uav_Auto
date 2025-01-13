from UAVAUTO_VERSION_4.config import db
from UAVAUTO_VERSION_4.Model.DroneStationMapping import DroneStationMapping

class DroneStationMappingController():
    @staticmethod
    def insert_drone_sation_mapping(data):
        drone_station_mapping = DroneStationMapping(station_id=data['station_id'],drone_id=data['drone_id'],status=data['status'])
        db.session.add(drone_station_mapping)
        db.session.commit()
        return drone_station_mapping

    @staticmethod
    def update_drone_station_mapping(drone_id,station_id):
        drone_station_mapping = DroneStationMapping.query.filter_by(drone_id=drone_id,validity=1).first()
        if drone_station_mapping:
            drone_station_mapping.station_id = station_id
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_drone_station_mapping_by_drone_id(drone_id):
        drone_station_mapping = DroneStationMapping.query.filter_by(drone_id=drone_id,validity=1).first()
        if drone_station_mapping:
            return {'id':drone_station_mapping.id,'drone_id':drone_station_mapping.drone_id,'station_id':drone_station_mapping.station_id,'status':drone_station_mapping.status}
        return {}
    @staticmethod
    def get_all_drone_station_mapping():
        drone_station_mappings = DroneStationMapping.query.filter_by(validity=1).all()
        return [{'id':d.id,'drone_id':d.drone_id,'station_id':d.station_id,'status':d.status} for d in drone_station_mappings]

    @staticmethod
    def delete_drone_station_mapping(drone_id):
        drone_station_mapping = DroneStationMapping.query.filter_by(drone_id=drone_id,validity=1).first()
        if drone_station_mapping:
            drone_station_mapping.validity = 0
            return {'id':drone_station_mapping.id,'drone_id':drone_station_mapping.drone_id,'station_id':drone_station_mapping.station_id,'status':drone_station_mapping.status}
        return {}