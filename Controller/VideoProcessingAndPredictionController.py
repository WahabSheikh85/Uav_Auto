import math
import os
from UAVAUTO_VERSION_4.Model.MissionTask import MissionTask
from fileinput import filename
from ultralytics import YOLO
import cv2
from  UAVAUTO_VERSION_4.Controller.MissionDataLocationController import MissionDataLocationController
from UAVAUTO_VERSION_4.Controller.MissionDataImageController import MissionDataImageController


class VideoProcessingAndPredictionController():

    def videoProcessingAndSaving(videoFiles, id, index):
        PathToSaveVideos = "E:/user/abdul wahab/PythonProjects/UAVAUTO_VERSION_4/uploads/Videos"
        # # Ensure the directory exists
        # if not os.path.exists(PathToSaveVideos):
        #     os.makedirs(PathToSaveVideos)

        for key, file in videoFiles.items():
            file_name = id + '_' + index + '_' + file.filename
            save_path = os.path.join(PathToSaveVideos, file_name)
            file.save(save_path)

        return "ok",200

    @staticmethod
    def prediction(id, index, speedofdrone, startLat, startLong):
        videoFps = 0
        totalFramesInVideo = 0
        duration = 0
        path = r'E:\user\abdul wahab\PythonProjects\UAVAUTO_VERSION_4\uploads\Videos'
        if not os.path.exists(path):
            raise FileNotFoundError(f"Directory not found: {path}")

        # Construct the video name prefix using id and index
        video_prefix = f"{id}_{index}_"

        # Filter videos that match the prefix
        video_files = [f for f in os.listdir(path) if
                       f.startswith(video_prefix) and f.endswith(('.mp4', '.avi', '.mkv'))]
        if not video_files:
            raise FileNotFoundError(f"No videos found with prefix: {video_prefix}")

        video_frames = {}

        for video_file in video_files:
            video_path = os.path.join(path, video_file)
            frames = []
            cap = cv2.VideoCapture(video_path)

            if not cap.isOpened():
                raise FileNotFoundError(f"Could not open video file: {video_path}")
            videoFps = cap.get(cv2.CAP_PROP_FPS)
            totalFramesInVideo = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            duration = totalFramesInVideo / videoFps

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                frames.append(frame)

            cap.release()

            # Store frames list in a dictionary with video name as key
            video_frames[video_file] = frames
        print('wahab')
        model = YOLO(
            'E:/user/abdul wahab/PythonProjects/ModelTraining1/runs/detect/custom_yolov11n_v1_moaaz/weights/best.pt')
        framesToReturn = []
        frameCount = 0
        secondsPassed = 0
        for k,v in video_frames.items():
            for frame in v:
                frameCount += 1
                if frameCount == int(videoFps):
                    secondsPassed += 1
                    frameCount = 0

                    results = model.predict(source=frame, save=False)
                    for result in results:
                        boxes = result.boxes
                        for box in boxes:
                            # each bb
                            # contains list of .cls (classes) sorted based on confidence scores ascending order
                            # contains list of .conf (confidence scores) sorted based on highest confidence scores ascending order
                            # and coordinates of bounding box .xyxy ([x_min, y_min, x_max, y_max])
                            cls = int(box.cls[0])
                            confidence = float(box.conf[0])
                            class_name = model.names[cls]
                            folderName = f'mission_{id}'
                            fileName = f'video_{index}'
                            output_path_main_dir = "E:/user/abdul wahab/PythonProjects/UAVAUTO_VERSION_4/ModelResults/" + folderName
                            output_path_sub_dir = output_path_main_dir + '/' + fileName
                            output_path_detected_images = output_path_sub_dir + '/DamageImages'
                            output_path_detected_lat_longs = output_path_sub_dir + '/LatLongs'
                            if class_name == 'damaged_pole':
                                print('wahab2')
                                distanceAtThisFrame = speedofdrone * secondsPassed

                                # Constants
                                R = 6371000  # Earth's radius in meters

                                # Convert starting latitude and longitude to radians
                                lat_start_rad = math.radians(startLat)
                                long_start_rad = math.radians(startLong)

                                # Calculate the change in latitude (delta_lat)
                                delta_lat = distanceAtThisFrame / R  # change in latitude in radians
                                lat_new_rad = lat_start_rad + delta_lat

                                # Calculate the change in longitude (delta_long), adjusting by latitude
                                delta_long = distanceAtThisFrame / (
                                            R * math.cos(lat_start_rad))  # change in longitude in radians
                                long_new_rad = long_start_rad + delta_long

                                # Convert the new latitude and longitude back to degrees
                                lat_new = math.degrees(lat_new_rad)
                                long_new = math.degrees(long_new_rad)

                                # Print the new latitude and longitude
                                print(f"distance travelled is{distanceAtThisFrame}")
                                print(f"New Latitude: {lat_new}, New Longitude: {long_new}")

                                if not os.path.exists(output_path_main_dir):
                                    os.makedirs(output_path_main_dir)
                                if not os.path.exists(output_path_sub_dir):
                                    os.makedirs(output_path_sub_dir)
                                if not os.path.exists(output_path_detected_images):
                                    os.makedirs(output_path_detected_images)
                                # if not os.path.exists(output_path_detected_lat_longs):
                                #     os.makedirs(output_path_detected_lat_longs)

                                framesToReturn.append(frame)
                                saveImageAs = f"E:/user/abdul wahab/PythonProjects/UAVAUTO_VERSION_4/ModelResults/mission_{id}/video_{index}/DamageImages/{lat_new}_{long_new}_{class_name}_{confidence:.2f}.jpg"
                                # saveLatLongAs = f"E:/user/abdul wahab/PythonProjects/UAVAUTO_VERSION_4/ModelResults/mission_{id}/video_{index}/LatLongs/{class_name}_{confidence:.2f}.jpg"
                                cv2.imwrite(saveImageAs, frame)
                                mission_task = MissionTask.query.filter_by(mission_planner_id=id).first()

                                dataToInsertLatLong = {
                                    'mission_task_id': mission_task.id,
                                    'latitude': lat_new,
                                    'longitude': long_new,
                                    'damage': 'damaged_pole'
                                }
                                response = MissionDataLocationController.insert_mission_data_location(dataToInsertLatLong)
                                print(response)
                                dataToInsertDamageImage = {
                                    'mission_data_location_id':response['id'],
                                    'image_path':saveImageAs
                                }
                                MissionDataImageController.insert_mission_data_image(dataToInsertDamageImage)
                                # print(f"Saved frame with damaged_pole at {output_path}")

                            # processedImage = result.plot()
                            # cv2.imshow('Detection', processedImage)
                            # cv2.waitKey(1)

        return 'ok',200

    @staticmethod
    def fetchImageResults():
        pass

