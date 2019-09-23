import cv2
class UpperBody:
    def __init__(self,courseid,sem,stream,caller,email):
        self.courseid=courseid
        self.sem=sem
        self.stream=stream
        self.caller=caller
        self.email=email
        self.new(self.courseid,self.sem,self.stream,self.caller,self.email)
    def new(self,courseid,sem,stream,caller,email):
        flag=0
        cam = cv2.VideoCapture(0)
        while(True):
            ret, img = cam.read()
            if(cv2.imwrite("input.jpg", img)):
                flag=1
            else:
                flag=0
            cv2.imshow('frame',img)
            if  cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cam.release()
        cv2.destroyAllWindows()    
        if(flag==1):
            print("ok")
            from imageserver import iserver
            iserver(courseid,stream,sem,email,caller)
        else:
            import tkMessageBox
            tkMessageBox.showwarning("Warning","Image Not Captured")

