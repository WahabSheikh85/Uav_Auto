from UAVAUTO_VERSION_4.config import db

class Drone(db.Model):
    __tablename__ = "Drone"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    speed = db.Column(db.Float, nullable=False, default=70)  # Speed in km/h
    flight_duration = db.Column(db.Float, nullable=False, default=1)  # Duration in hours
    ceiling = db.Column(db.Float, nullable=False)  # Max altitude in meters
    fps = db.Column(db.Integer, nullable=False)  # Frames per second for cameras
    image_path = db.Column(db.String(300), nullable=True)  # Nullable to allow flexibility
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationships
    drone_availability_logs = db.relationship('DroneAvailabilityLog', back_populates='drone')  # Matches DroneAvailabilityLog model
    drone_station_mappings = db.relationship('DroneStationMapping', back_populates='drone')  # Matches DroneStationMapping model
    mission_planners = db.relationship('MissionPlanner', back_populates='drone')  # Matches MissionPlanner model
