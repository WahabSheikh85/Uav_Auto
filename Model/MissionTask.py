from UAVAUTO_VERSION_4.config import db

class MissionTask(db.Model):
    __tablename__ = "mission_task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_planner_id = db.Column(db.Integer, db.ForeignKey('mission_planner.id'), nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey('Routes.id'), nullable=False)
    description = db.Column(db.String(1000), nullable=False)  # Task description
    validity = db.Column(db.Integer, nullable=False, default=1)  # Active status: 1 for valid, 0 for invalid

    # Relationship with MissionPlanner
    mission_planner = db.relationship('MissionPlanner', back_populates='mission_tasks')  # Matches MissionPlanner model

    # Relationship with MissionDataLocation
    mission_data_locations = db.relationship('MissionDataLocation', back_populates='mission_task')  # Plural for one-to-many

    # Relationship with Routes
    route = db.relationship('Routes', back_populates='mission_tasks')  # Matches Routes model
