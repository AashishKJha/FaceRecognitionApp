import mysql.connector
import datetime
                    
class database:
    def __init__(self,list_detect,branch,s):
        self.list_detect=list_detect
        self.branch=branch
        self.s=s
    def WOL(self):
        name=''
        name1=''
        out=''
        out_not=''
        i=0
        new_list=[]
        papa=[]
        cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
        if(cnx):
            cursor=cnx.cursor()
            q1="select count(*) from sregister"
            cursor.execute(q1)
            result1=cursor.fetchone()
            t_row=int(result1[0])

            while(i<len(self.list_detect)):
                x=str(self.list_detect[i])
                y=str(x[0])+str(x[1])+str(self.branch)+str(x[2])+str(x[3])
                new_list.append(y)
                q="select fname,mname,sname from sregister where cid=%s"
                
                data=(y,)
                cursor.execute(q,data)
                result=cursor.fetchone()
                name=str(result[0])+" "+str(result[1])+" "+str(result[2])+"/"+str(y)
                out=out+name+"//"

                i=i+1
            cnx.commit()

##            now=datetime.datetime.now()
##            reg_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
##            reg_time=str(str(now.hour)+":"+str(now.minute)+":"+str(now.second))

            i=0
            while(i<len(new_list)):
                q4="UPDATE attendance_m SET att_date=CURDATE(),mark=1 where cid=%s"
                data1=(str(new_list[i]),)
                cursor.execute(q4,data1)
                i=i+1
            cnx.commit()
            
            
            i=0
            q="select cid from attendance_m where mark=%s"
            data5=(int(0),)
            cursor.execute(q,data5)
            result2=cursor.fetchall()
            cnx.commit()
            i=0

            

            while(i<len(result2)):
                
                q="select fname,mname,sname,cid from sregister where cid=%s"
                data3=(str(result2[i][0]),)
                cursor.execute(q,data3)
                result3=cursor.fetchall()
                papa.append(result3)
                i=i+1
            cnx.commit()
            #str(result3[i][0][0])+" "+str(result3[i][0][1])+" "+str(result3[i][0][2])+"/"+str(result3[i][0][3])
            i=0
            while(i<len(papa)):
                out_not=out_not+str(papa[i][0][0]+" "+papa[i][0][1]+" "+papa[i][0][2]+"/"+papa[i][0][3])+"//"
                i=i+1
            
            
            
            
            cursor.close()
            cnx.close()
            
            return(str(out+"@"+out_not+"@@"))
        else:
            import tkMessageBox
            tkMessageBox.showwarning("Warning","Error")
                    
                    
            
        
        
        
