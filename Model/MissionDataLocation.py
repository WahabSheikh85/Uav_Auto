from UAVAUTO_VERSION_4.config import db

class MissionDataLocation(db.Model):
    __tablename__ = 'mission_data_location'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_task_id = db.Column(db.Integer, db.ForeignKey('mission_task.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)  # Latitude of the damage location
    longitude = db.Column(db.Float, nullable=False)  # Longitude of the damage location
    damage = db.Column(db.String(50), nullable=False)  # Description of the damage (e.g., type of fault)
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationship with MissionTask
    mission_task = db.relationship('MissionTask', back_populates='mission_data_locations')  # Matches MissionTask model

    # Relationship with MissionDataImage
    mission_data_images = db.relationship('MissionDataImage', back_populates='mission_data_location')  # Plural for one-to-many
