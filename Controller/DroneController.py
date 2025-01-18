from UAVAUTO_VERSION_4.config import db
from UAVAUTO_VERSION_4.Model.Drone import Drone
from UAVAUTO_VERSION_4.Controller.DroneStationMappingController import DroneStationMappingController
from UAVAUTO_VERSION_4.Controller.StationController import StationController
import os
import numpy as np
class DroneController():
    @staticmethod
    def insert_drone(data, image):
        path = r'E:\user\abdul wahab\PythonProjects\UAVAUTO_VERSION_4\uploads\DroneImageData'

        name = str(np.random.randint(0, 100000000)) + '_' + image.filename
        path = os.path.join(path, name)
        drone = Drone(name=data['name'],speed=data['speed'],flight_duration=data['flight_duration'],ceiling=data['ceiling'],fps=data['fps'],image_path=path)
        image.save(path)
        db.session.add(drone)
        db.session.commit()
        newData = {
            'station_id':data['station_id'],
            'drone_id':drone.id,
            'status':1
        }
        drone_station_mapping = DroneStationMappingController.insert_drone_sation_mapping(newData)
        update_drone_nums = StationController.increment_num_drones(data['station_id'])
        return drone,drone_station_mapping

    @staticmethod
    def upload_drone_image(data):
        admin_id = data['admin_id']

    @staticmethod
    def delete_drone(drone_id):
        drone = Drone.query.get_or_404(drone_id)
        if drone:
            drone.validity = 0
            db.session.commit()
            drone_station_mapping = DroneStationMappingController.delete_drone_station_mapping(drone_id)
            StationController.decrement_num_drones(drone_station_mapping.get('station_id'))
            return True
        return False

    @staticmethod
    def update_drone(data):
        drone = Drone.query.get_or_404(data.get('drone_id'))
        if drone:
            drone_station_mapping = DroneStationMappingController.get_drone_station_mapping_by_drone_id(data.get('drone_id'))
            print('drone_station_mapping',drone_station_mapping)
            if drone_station_mapping:
                StationController.decrement_num_drones(drone_station_mapping.get('station_id'))

            drone.name = data.get('name',drone.name)
            drone.speed = data.get('speed',drone.speed)
            drone.ceiling = data.get('ceiling',drone.ceiling)
            drone.flight_duration = data.get('flight_duration',drone.flight_duration)
            drone.fps = data.get('fps',drone.fps)
            drone.image_path = data.get('image_path',drone.image_path)
            db.session.commit()
            is_drone_station_mapping_updated = DroneStationMappingController.update_drone_station_mapping(drone.id,data.get('station_id'))
            StationController.increment_num_drones(data.get('station_id'))

            return {'id':drone.id,'name':drone.name,'ceiling':drone.ceiling,'flight_duration':drone.flight_duration,'fps':drone.fps,'speed':drone.speed,'image_path':drone.image_path}
        return {}
    @staticmethod
    def get_all_drones():
        drones = Drone.query.filter_by(validity=1).all()
        return [{'id':d.id,'name':d.name,'speed':d.speed,'flight_duration':d.flight_duration,'ceiling':d.ceiling,'fps':d.fps,'image_path':d.image_path} for d in drones]

