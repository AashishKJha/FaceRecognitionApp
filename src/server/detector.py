import cv2
import numpy as np
import mysql

class detect:
    def __init__(self,course,sem,branch,s):
        self.branch=branch
        self.course=course
        self.sem=sem
        self.s=s
    def detection(self):
        detected=[]
        emp1=[]
        import mysql.connector
        cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
        if(cnx):
            cursor=cnx.cursor()
            try:
                q=("select cid from sregister where course=%s AND sem=%s AND stream=%s ")
                data=(str(self.course),str(self.sem),str(self.branch))
                
                cursor.execute(q,data)
                result=cursor.fetchall()
                cnx.commit()
                print(result)
                i=0
                while(i<len(result)):
                    x=str(result[i][0])
                    print(x)
                    y=str(x[0])+str(x[1])+str(x[4])+str(x[5])
                    print(y)
                    emp1.append(y)
                    i=i+1
                print(emp1)
            except Exception as e:
                print(str(e)+"---"+str(type(e)))
            cursor.close()
        cnx.close()


        faceDetect= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        rec=cv2.createLBPHFaceRecognizer()
        rec.load("Trainner\\trainner.yml")
        id=0

        img=cv2.imread('input.jpg')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        kernel_sharpen_3 = np.array([[-1,-1,-1,-1,-1],
                                     [-1,2,2,2,-1],
                                     [-1,2,8,2,-1],
                                     [-1,2,2,2,-1],
                                     [-1,-1,-1,-1,-1]]) / 8.0

        output_3 = cv2.filter2D(gray, -1, kernel_sharpen_3)



        faces = faceDetect.detectMultiScale(output_3, 1.3, 5)
        

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)


            id,conf=rec.predict(output_3[y:y+h,x:x+w])
            i=0
            print(len(emp1))

            while(i<len(emp1)):
                if((conf<100) and (str(id)==str(emp1[i]))):
                    print("ok")
                    detected.append(id)
                i=i+1
            print(detected)
            
                
        if(len(detected)!=0):
##            from datalist import database
##            print(detected)
##            database(detected,branch,s)
            return(detected,self.branch,self.s)
        else:
            print("face not detected")
                
