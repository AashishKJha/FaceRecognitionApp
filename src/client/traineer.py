import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
##detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
path="C:/Users/ASHISH KR. JHA/Documents/Desktop/Python1/project/Photo/DataSetPics/BTech/CS/SEMESTER 8"

def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])

##        faces=detector.detectMultiScale(imageNp)
##        for (x,y,w,h) in faces:
##            faces.append(imageNp[y:y+h,x:x+w])
##            IDs.append(ID)
        faces.append(faceNp)
        print ID
        IDs.append(ID)
        cv2.imshow("training",faceNp)
        cv2.waitKey(10)
    return IDs,faces



Ids,faces = getImagesWithID(path)
recognizer.train(faces, np.array(Ids))
recognizer.save('Trainner/trainner.yml')
cv2.destroyAllWindows()
