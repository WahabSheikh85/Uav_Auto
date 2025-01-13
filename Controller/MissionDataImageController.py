from UAVAUTO_VERSION_4.config import db,app
from UAVAUTO_VERSION_4.Model.MissionDataImage import MissionDataImage
import os
from UAVAUTO_VERSION_4.ProcessImage import process_single_image,process_video,extract_frames
from io import BytesIO
from PIL import Image
class MissionDataImageController():
    @staticmethod
    def insert_mission_data_image(data):
        mission_data_image = MissionDataImage(mission_data_location_id=data['mission_data_location_id'],image_path = data['image_path'])
        db.session.add(mission_data_image)
        db.session.commit()
        return mission_data_image
    @staticmethod
    def upload_image(data):
        processesed_image_path,isDamaged = process_single_image(data)
        # print("PROCESSSED IMAGE",processesed_image_path,type(processesed_image_path))
        # data_path = os.path.join(app.config['UPLOAD_FOLDER'],data.filename)
        # data.save(data_path)
        return processesed_image_path

    @staticmethod
    def upload_video(data):
        temp_folder = './temp_video_images'
        os.makedirs(temp_folder,exist_ok=True)
        output_folder = './Extracted_frames'
        os.makedirs(output_folder,exist_ok=True)
        full_path = os.path.join(temp_folder,'temp_video.mp4')
        print("FULL PATH:",full_path)
        data.save(full_path)
        extract_frames(full_path,output_folder,1)




