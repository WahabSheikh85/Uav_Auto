from UAVAUTO_VERSION_4.config import db

class MissionDataImage(db.Model):
    __tablename__ = 'mission_data_image'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_data_location_id = db.Column(db.Integer, db.ForeignKey('mission_data_location.id'), nullable=False)
    image_path = db.Column(db.String(300), nullable=False)  # Path to the image file
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationship with MissionDataLocation
    mission_data_location = db.relationship('MissionDataLocation', back_populates='mission_data_images')  # Matches MissionDataLocation
