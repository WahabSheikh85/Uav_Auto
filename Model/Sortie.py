from UAVAUTO_VERSION_4.config import db
from datetime import date, datetime

class Sortie(db.Model):
    __tablename__ = 'Sortie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mission_planner_id = db.Column(db.Integer, db.ForeignKey('mission_planner.id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False, default=date.today)
    end_date = db.Column(db.Date, nullable=True)  # Nullable to handle ongoing sorties
    start_time = db.Column(db.Time, nullable=False, default=lambda: datetime.now().time())
    end_time = db.Column(db.Time, nullable=True)  # Nullable to handle ongoing sorties
    duration = db.Column(db.Float, nullable=True)  # Nullable, calculated after sortie ends
    validity = db.Column(db.Integer, nullable=False, default=1)  # 1 for valid, 0 for invalid

    # Relationship with MissionPlanner
    mission_planner = db.relationship('MissionPlanner', back_populates='sorties')  # Matches MissionPlanner model
