import os
import cv2

#------------------------------------------------------------------------------------

global fileLoc
fileLoc="userData/"

#------------------------------------------------------------------------------------

def takePhoto():
    cam = cv2.VideoCapture(0)
    ret,frame = cam.read()
    imageFilename = fileLoc+"faceData.jpg"
    cv2.imwrite(imageFilename, frame)    
    cam.release()
