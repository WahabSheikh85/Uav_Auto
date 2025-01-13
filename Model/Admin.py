from UAVAUTO_VERSION_4.config import db

class Admin(db.Model):
    __tablename__ = "Admin"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)  # Changed to String for better compatibility with phone numbers
    validity = db.Column(db.Integer, nullable=False, default=1)

    # Relationship with User
    user = db.relationship('User', back_populates='admin')

    # Relationship with MissionPlanner
    mission_planners = db.relationship('MissionPlanner', back_populates='admin')  # Pluralized for consistency

    # Relationship with Routes
    routes = db.relationship('Routes', back_populates='admin')
