from UAVAUTO_VERSION_4.config import db

class Station(db.Model):
    __tablename__ = 'Station'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)  # Latitude of the station
    longitude = db.Column(db.Float, nullable=False)  # Longitude of the station
    num_drones = db.Column(db.Integer, nullable=False, default=0)  # Number of drones at the station
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationships
    drone_station_mappings = db.relationship('DroneStationMapping', back_populates='station')  # Matches DroneStationMapping model
