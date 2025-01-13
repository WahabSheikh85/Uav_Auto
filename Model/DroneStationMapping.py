from UAVAUTO_VERSION_4.config import db

class DroneStationMapping(db.Model):
    __tablename__ = "drone_station_mapping"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.Integer, db.ForeignKey('Station.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)  # Boolean indicating drone availability at the station
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationships
    drone = db.relationship('Drone', back_populates='drone_station_mappings')  # Matches Drone model
    station = db.relationship('Station', back_populates='drone_station_mappings')  # Matches Station model
