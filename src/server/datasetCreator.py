import cv2
class datasetcreat:
    def __init__(self,cid,courseid,sem,stream):
        self.cid=cid
        self.courseid=courseid
        self.sem=sem
        self.stream=stream
        self.new(self.cid,self.courseid,self.sem,self.stream)
    def new(self,cid,courseid,sem,stream):
        cam = cv2.VideoCapture(0)
        detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
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
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                
                sampleNum=sampleNum+1
                cv2.imwrite("Photo/DataSetPics/"+courseid+"/"+stream+"/"+sem+"/"+str(id) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

                cv2.imshow('Picture',img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            elif sampleNum>19:
                break
        cam.release()
        cv2.destroyAllWindows()
