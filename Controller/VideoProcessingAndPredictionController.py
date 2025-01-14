import os
from fileinput import filename
from ultralytics import YOLO
import cv2

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
    def prediction(id, index):
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
        for k,v in video_frames.items():
            for frame in v:
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
                        if class_name == 'damaged_pole':
                            print('wahab2')

                            if not os.path.exists(output_path_main_dir):
                                os.makedirs(output_path_main_dir)
                            if not os.path.exists(output_path_sub_dir):
                                os.makedirs(output_path_sub_dir)

                            framesToReturn.append(frame)
                            saveImageAs = f"E:/user/abdul wahab/PythonProjects/UAVAUTO_VERSION_4/ModelResults/mission_{id}/video_{index}/{class_name}_{confidence:.2f}.jpg"
                            cv2.imwrite(saveImageAs, frame)
                            # print(f"Saved frame with damaged_pole at {output_path}")

                        processedImage = result.plot()
                        cv2.imshow('Detection', processedImage)
                        cv2.waitKey(1)







        return 'ok',200

    @staticmethod
    def fetchImageResults():
        pass

