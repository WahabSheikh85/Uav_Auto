
from ultralytics import YOLO
import cv2
import numpy as np
import os
from config import app




model = YOLO(r'E:\user\abdul wahab\PythonProjects\UAVAUTO_VERSION_4\CVModel\weights\best.pt')  # Path to your trained weights

# Function to process a single image

# def process_single_image(image):
#     # Convert image from file to array
#     img_array = np.frombuffer(image.read(), np.uint8)
#     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
#
#     # Predict using YOLO model
#     result = model.predict(source=img, save=False)
#     plotted_image = []
#     isDamaged = False
#     for r in result:
#         # Get labels, bounding boxes, and confidence scores
#         labels = r.names  # Predicted class names
#         bboxes = r.boxes.xyxy  # Bounding boxes (x_min, y_min, x_max, y_max)
#         confidences = r.boxes.conf  # Confidence scores
#         class_ids = r.boxes.cls  # Class IDs
#
#         print("Labels:", labels)
#         print("Bounding Boxes:", bboxes)
#         print("Confidence Scores:", confidences)
#         print("Class IDs:", class_ids)
#         for cls in class_ids:
#             cls = int(cls)
#             if(labels[cls]=='damaged_pole' or labels[cls]=='damaged_wire' or labels[cls]=='damaged_insulator' or labels[cls]=='loose_wire'):
#                 # Plot and display the predictions
#                 plotted_image = r.plot()
#                 isDamaged = True
#
#         # cv2.imshow('Predictions', plotted_image)
#         # cv2.waitKey(0)
#         # cv2.destroyAllWindows()
#
#     temp_path = os.path.join(app.config['TEMP_FOLDER'], "processed_image.jpg")
#     cv2.imwrite(temp_path, plotted_image)
#     # Get the absolute path
#     absolute_path = os.path.abspath(temp_path)
#     if isDamaged:
#         return absolute_path,True
#     else:
#         return absolute_path,False
#     # return result

# Function to process multiple images
def process_multiple_images(images):
    processed_paths = []

    for image in images:
        # Process each image
        img_array = np.frombuffer(image.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        result = model.predict(source=img, save=False)

        # Plot predictions
        for pred_img in result:
            processed_img = pred_img.plot()

        # Save each processed image temporarily
        temp_path = os.path.join(app.config['TEMP_FOLDER'], f"processed_image_{len(processed_paths)}.jpg")
        cv2.imwrite(temp_path, processed_img)
        processed_paths.append(temp_path)

    return processed_paths

def process_video():
    pass

def extract_frames(video_path,output_folder,extract_interval=1):
    cap = cv2.VideoCapture(video_path)
    # Get the frame rate (FPS) of the video
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"Frames per second: {fps}")

    # Calculate frame interval (number of frames to skip)
    frame_interval = fps * extract_interval
    frame_count = 0
    saved_frame_count = 0
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            plotted_image,isDamaged = process_single_image(frame)
            frame_file_name = os.path.join(output_folder,f"frame_{saved_frame_count}.jpeg")
            cv2.imwrite(frame_file_name,plotted_image)
            saved_frame_count+=1
            # if isDamaged:
            #     frame_file_name = os.path.join(output_folder,f"frame_{saved_frame_count}.jpeg")
            #     cv2.imwrite(frame_file_name,plotted_image)
            #     saved_frame_count+=1
        frame_count+=1

    cap.release()
    print(f"saved frame count is:{saved_frame_count}")

def process_single_image(img):
    # Convert image from file to array
    # img_array = np.frombuffer(image.read(), np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    # Predict using YOLO model
    result = model.predict(source=img, save=False)
    plotted_image = []
    isDamaged = False
    for r in result:
        # Get labels, bounding boxes, and confidence scores
        labels = r.names  # Predicted class names
        bboxes = r.boxes.xyxy  # Bounding boxes (x_min, y_min, x_max, y_max)
        confidences = r.boxes.conf  # Confidence scores
        class_ids = r.boxes.cls  # Class IDs

        # print("Labels:", labels)
        # print("Bounding Boxes:", bboxes)
        # print("Confidence Scores:", confidences)
        # print("Class IDs:", class_ids)
        for cls in class_ids:
            cls = int(cls)
            if(labels[cls]=='damaged_pole' or labels[cls]=='damaged_wire' or labels[cls]=='damaged_insulator' or labels[cls]=='loose_wire'):
                # Plot and display the predictions
                isDamaged = True
            plotted_image = r.plot()

        # cv2.imshow('Predictions', plotted_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    # temp_path = os.path.join(app.config['TEMP_FOLDER'], "processed_image.jpg")
    # cv2.imwrite(temp_path, plotted_image)
    # Get the absolute path
    # absolute_path = os.path.abspath(temp_path)
    if isDamaged:
        return plotted_image,True
    else:
        return plotted_image,False

