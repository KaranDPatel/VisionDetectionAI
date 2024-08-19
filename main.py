import cv2
from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

video=cv2.VideoCapture("testvideo.mp4")

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

net=cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt','MobileNetSSD_deploy.caffemodel')


while True:
    ret,frame=video.read()
    frame=cv2.resize(frame,(640,480))
    (h,w)=frame.shape[:2]
    blob=cv2.dnn.blobFromImage(cv2.resize(frame,(300,300)),0.007843, (300,300),127.5)
    net.setInput(blob)
    detection=net.forward()
    print(detection)
    for i in np.arange(0,detection.shape[2]):
        confidence=detection[0,0,i,2]
        if confidence>0.5:
            id=detection[0,0,i,1]
            box=detection[0,0,i,3:7]* np.array([w,h,w,h])
            (startX,starY,endX,endY)=box.astype("int")
            cv2.rectangle(frame,(startX,starY),(endX,endY),(0,255,0))
            cv2.putText(frame,CLASSES[int(id)],(startX+10,starY-15),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,0.7,(255,255,255))
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k == ord('q'):
        break
video.release()
cv2.destroyAllWindows()