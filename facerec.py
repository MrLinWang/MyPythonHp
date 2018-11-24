import numpy
import cv2

def Getface(image):
    cvo = cv2.CascadeClassifier('haarcascade_fronttalface_default.xml')
    cvo.load('C:/ProgramData/Anaconda2/pkgs/opencv-3.3.0/data/haarcascades/haarcascade_fronttalface_default.xml')
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = cvo.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

    return image

cam = cv2.VideoCapture(0)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4',fourcc,20.0,(width,height))

while(cam.isOpened()):
    ret,frame = cam.read()
    if ret == True:
        frame = Getface(frame)
        out.write(frame)

        cv2.imshow('My Camera',frame)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break
    else:
        break

out.release()
cam.release()
cv2.destroyAllWindows()
