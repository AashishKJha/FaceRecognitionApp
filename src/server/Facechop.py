import cv2
import PIL
from PIL import Image

facedata = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(facedata)
image="C:\\Users\\Aditya\\Desktop\\Project\\Main\\input.jpg"
sampleNum=0


basewidth=720
img=Image.open(image)
wpercent=(basewidth/float(img.size[0]))
hsize=int((float(img.size[1])*float(wpercent)))
img=img.resize((basewidth,hsize),PIL.Image.ANTIALIAS)
img.save('output.jpg')

mainimage=('C:\\Users\\Aditya\\Desktop\\Project\\Main\\output.jpg')

img=cv2.imread(mainimage)


gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)

for f in faces:
    x, y, w, h = [ v for v in f ]
    #cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,255))

    sub_face = img[y:y+h, x:x+w]
##    sub_face= cv2.cvtColor(sub_face,cv2.COLOR_BGR2GRAY)
    sampleNum=sampleNum+1
    face_file_name = "TempFaces/Face" + str(sampleNum) + ".jpg"
    cv2.imwrite(face_file_name, sub_face)


