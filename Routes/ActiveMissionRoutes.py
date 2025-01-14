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
    lat = request.form.get('lat')
    long = request.form.get('long')
    VideoProcessingAndPredictionController.videoProcessingAndSaving(videoFiles=videoFiles, id=missionPlannerId, index=index)
    VideoProcessingAndPredictionController.prediction(missionPlannerId, index)
    return 'ok',200
