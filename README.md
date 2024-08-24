**Object Detection Using MobileNetSSD**

**Overview**

This project demonstrates a basic object detection system using the MobileNetSSD deep learning model. The system is capable of detecting various objects, such as cars, animals, and people, in video streams or individual frames. The project leverages OpenCV and the MobileNetSSD pre-trained model to identify and annotate objects in real-time.

**Features**

Real-Time Object Detection: Detects objects in real-time from a video feed or video file.

Pre-Trained Model: Utilizes the MobileNetSSD model, pre-trained on the VOC dataset, for efficient object detection.

Multiple Object Classes: Capable of detecting 20 different object classes, including vehicles, animals, and furniture.

User-Friendly Interface: Provides real-time visualization of detected objects with bounding boxes and labels.

**Prerequisites**

Python 3.x installed on your system.

Required Python packages: opencv-python, matplotlib, numpy.

**Installation**

Clone the Repository:

- git clone url

**Install Required Python Packages:**

- pip install opencv-python matplotlib numpy
   
Download the Pre-Trained Model:

Ensure you have the following files in the project directory:

MobileNetSSD_deploy.prototxt.txt

MobileNetSSD_deploy.caffemodel

You can download them from the official Caffe Model Zoo.

Usage

Run the Object Detection Script:
- python object_detection.py

Video Input:
The script processes a video file named testvideo.mp4. Replace this with your video file for custom input.

Object Detection in Real-Time:

The script will open a window displaying the video with detected objects highlighted by bounding boxes and labels.

Press q to quit the video feed and close the window.

File Structure

object-detection-mobilenetssd/

├── object_detection.py         # Main script for object detection

├── MobileNetSSD_deploy.prototxt.txt  # Model configuration file

├── MobileNetSSD_deploy.caffemodel    # Pre-trained model weights

├── testvideo.mp4               # Sample video file

├── README.md                   # This readme file

└── requirements.txt            # List of Python dependencies (if applicable)

**Customization**

Confidence Threshold: Adjust the confidence threshold for detecting objects by modifying the confidence > 0.5 line in the script.

Input Source: Change the video input by replacing "testvideo.mp4" with the path to your video file or by integrating live video capture from a webcam.

Object Classes: The model is pre-trained to detect 20 different object classes. You can modify the CLASSES list to add or remove labels based on your application needs.
