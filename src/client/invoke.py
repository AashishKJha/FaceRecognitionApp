import numpy as np 
import cv2
class Invoke:
        def __init__(self,cid):
                self.cid=cid
                self.new(self.cid)

        def new(self,cid):
                camera=cv2.VideoCapture(0)
                face_cascade = cv2.CascadeClassifier("C:\\Users\\ASHISH KR. JHA\\Documents\\Desktop\\Python1\\HS.xml")
                while(camera.isOpened()):
                        ret,image=camera.read()
                        pho = cv2.flip(image,1)
                        image = cv2.flip(image,1)
                        
                        if ret == True:
                                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                                faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                                for (x,y,w,h) in faces:
                                        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
                                        pass
                                
                        cv2.imshow('image',image)
                        if cv2.waitKey(20) & 0xFF == ord('s'):
                                for (x,y,w,h) in faces:
                                        name = "C:/Users/ASHISH KR. JHA/Documents/Desktop/Python1/pic/" + str(cid) +".jpg"
                                        imga = pho[y:y+h, x:x+w]                
                                        cv2.imwrite(name, imga)
                                        cv2.imshow('Capture Face', imga)
                                        key = cv2.waitKey(0) & 0xFF
                                        
                                        
                                        if key == 27:
                                                break;
                                break
                                camera.release()
                                break
                cv2.destroyAllWindows()

