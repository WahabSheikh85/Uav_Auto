from UAVAUTO_VERSION_4.config import db


class Routes(db.Model):
    __tablename__ = "Routes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('Admin.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    validity = db.Column(db.Integer, nullable=False, default=1)

    # Relationship with Admin
    admin = db.relationship("Admin", back_populates='routes')

    # Relationship with LocationPin
    location_pin = db.relationship('LocationPin', back_populates='routes')

    # Relationship with MissionTask
    mission_tasks = db.relationship('MissionTask', back_populates='route')  # Use a meaningful plural name
