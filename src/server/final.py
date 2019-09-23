import mysql.connector
import datetime

class Final_att:
    def __init__(self,strng):
        self.strng=strng
        self.marked(self.strng)
    def marked(self,strng):
        x=strng.split("/")
        i=0
        cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
        cursor=cnx.cursor()
        if(cnx):
            
            while(i<(len(x)-1)):
                q4="UPDATE attendance_m SET att_date=CURDATE(),mark=1 where cid=%s"
                data1=(str(x[i]),)
                print(data1)
                cursor.execute(q4,data1)
                i=i+1
            cnx.commit()
        cursor.close()
        cnx.close()
