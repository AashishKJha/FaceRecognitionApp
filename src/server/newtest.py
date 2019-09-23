import cv2
class UpperBody:
    def __init__(self,cid,courseid,sem,stream):
        self.cid=cid
        self.courseid=courseid
        self.sem=sem
        self.stream=stream
        self.new(self.cid,self.courseid,self.sem,self.stream)
    def new(self,cid,courseid,sem,stream):
        
        cam = cv2.VideoCapture(0)
        detector=cv2.CascadeClassifier('HS.xml')
        y=list(cid.upper())
        i=0
        j=0
        q=[]
        x="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        x=list(x)
        while(i<len(y)):
            p=y[i] in x
            if(p==False):
                q.append(y[i])
            i=i+1
        i=0
        st=""
        while(i<len(q)):
            st=st+q[i]
            i=i+1
        id=int(st)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            if ret==True:
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                
                cv2.imwrite("Photo/FullImage/"+courseid+"/"+stream+"/"+sem+"/"+str(id)+ ".jpg", img)

                cv2.imshow('frame',img)
                if  cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        cv2.destroyAllWindows()
UpperBody('13cs03','BTech','SEMESTER 8','CS')
