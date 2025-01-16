from operator import index

from flask import Blueprint,jsonify,request
import os
from UAVAUTO_VERSION_4.Controller.VideoProcessingAndPredictionController import VideoProcessingAndPredictionController
active_mission_routes = Blueprint('active_mission_routes',__name__)
@active_mission_routes.route('/processVideo', methods=['GET'])
def receivedVideos():
    videoFiles = request.files
    missionPlannerId = request.form.get('id')
    index = request.form.get('index')
    speedOfDrone = int(request.form.get('speed'))
    lat = float(request.form.get('lat'))
    long = float(request.form.get('long'))
    VideoProcessingAndPredictionController.videoProcessingAndSaving(videoFiles=videoFiles, id=missionPlannerId, index=index)
    VideoProcessingAndPredictionController.prediction(id=missionPlannerId, index=index, speedofdrone=speedOfDrone, startLat=lat, startLong=long)
    return 'ok',200
