from UAVAUTO_VERSION_4.config import db

class Operator(db.Model):
    __tablename__ = "Operator"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    image_path = db.Column(db.String(500), nullable=True)  # Optional image path for operator profile
    validity = db.Column(db.Integer, nullable=False, default=1)

    # Relationship with User
    user = db.relationship('User', back_populates='operator')

    # Relationship with MissionPlanner
    mission_planners = db.relationship('MissionPlanner', back_populates='operator')  # Pluralized for one-to-many
