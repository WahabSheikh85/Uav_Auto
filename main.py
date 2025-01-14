from UAVAUTO_VERSION_4.config import app, db
from UAVAUTO_VERSION_4.Routes import active_mission_routes,user_routes,drone_routes,mission_planner_routes,mission_task_routes,location_pin_routes,mission_data_location_routes,mission_data_image_routes,sortie_routes,drone_availability_log_routes,drone_station_mapping_routes,station_routes,mission_station_mapping_routes,routes_controller_routes
import os

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'],exist_ok=True)

# Create a directory to temporarily store processed images
TEMP_FOLDER = './temp_images'
app.config['TEMP_FOLDER'] = TEMP_FOLDER
os.makedirs(TEMP_FOLDER, exist_ok=True)

# app.register_blueprint(user_routes, url_prefix='/api')  # Optional: prefix all user routes with '/api'
app.register_blueprint(user_routes)  # Optional: prefix all user routes with '/api'
app.register_blueprint(drone_routes)
app.register_blueprint(mission_planner_routes)
app.register_blueprint(mission_task_routes)
app.register_blueprint(location_pin_routes)
app.register_blueprint(mission_data_location_routes)
app.register_blueprint(mission_data_image_routes)
app.register_blueprint(sortie_routes)
app.register_blueprint(drone_availability_log_routes)
app.register_blueprint(drone_station_mapping_routes)
app.register_blueprint(station_routes)
app.register_blueprint(mission_station_mapping_routes)
app.register_blueprint(routes_controller_routes)
app.register_blueprint(active_mission_routes)
if __name__ == "__main__":
    app.run(debug=True)
