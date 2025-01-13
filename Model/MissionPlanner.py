from UAVAUTO_VERSION_4.config import db
from datetime import datetime, date

class MissionPlanner(db.Model):
    __tablename__ = "mission_planner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('Admin.id'), nullable=False)
    drone_id = db.Column(db.Integer, db.ForeignKey('Drone.id'), nullable=False)
    operator_id = db.Column(db.Integer, db.ForeignKey('Operator.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    start_time = db.Column(db.Time, nullable=False, default=lambda: datetime.now().time())
    status = db.Column(db.String(100), nullable=False, default='not set')  # Example statuses: 'not set', 'in progress', 'completed'
    validity = db.Column(db.Integer, nullable=False, default=1)  # 1 for valid, 0 for invalid

    # Relationships
    admin = db.relationship('Admin', back_populates='mission_planners')  # Relationship with Admin
    operator = db.relationship('Operator', back_populates='mission_planners')  # Relationship with Operator
    drone = db.relationship('Drone', back_populates='mission_planners')  # Relationship with Drone
    mission_tasks = db.relationship('MissionTask', back_populates='mission_planner')  # One-to-many with MissionTask
    sorties = db.relationship('Sortie', back_populates='mission_planner')  # One-to-many with Sortie
