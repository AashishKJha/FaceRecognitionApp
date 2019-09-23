import numpy as np
import cv2

faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
##cam = cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer();
img=cv2.imread("C:\\Users\\Aditya\\Desktop\\Project\\Main\\TempFaces\\Face1.jpg")
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceDetect.detectMultiScale(gray,1.3,5)
rec.load("Trainner\\trainner.yml")
#img=cv2.imread("C:\\Users\\Aditya\\Desktop\\Project\\Main\\TempFaces\\Face1.jpg")


print(gray)
for (x, y, w, h) in faces:
    
##    ret,img = cam.read()
##    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
##    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
##    for (x,y,w,h) in faces:
##        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    id,conf=rec.predict(gray[y: y + h, x: x + w])
    print(str(id))
    if(id==2):
        print("Aashish")
    if(id==1):
        print("Aditya")
    if(id==3):
        print("Manoj")
##    cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
##    cv2.imshow('Face',img)
    if cv2.waitKey(1) == ord('q'):
        break
    
##cam.release()
cv2.destroyAllWindows()
