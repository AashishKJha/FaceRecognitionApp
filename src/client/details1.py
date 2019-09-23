import Tkinter
from Tkinter import *
import tkFont
import ttk
import datetime
from datetime import date
import calendar
import PIL
from PIL import Image
class Detailsstudent:
    try:
        def __init__(self,mwindow,cid):
            self.new(mwindow,cid)
        def new(self,caller,cid):
            mwindow=Toplevel(caller)
            mwindow.title("ATTENDANCE SHEET")
            mwindow.configure(height=650,width=900,bg="#FF33FF")
            mwindow.minsize(height=650,width=900)
            mwindow.maxsize(height=650,width=900)
            menu=Menu(mwindow)
            menu1=Menu(menu,activebackground="pink",tearoff=0)
            menu.add_cascade(menu=menu1,label="Admin")
            menu.add_command(label="System Guide")
            help1=Menu(menu,activebackground="pink",tearoff=0)
            menu.add_cascade(menu=help,label="help")
            help1.add_command(label="About Us")
            mwindow['menu']=menu

            f=tkFont.Font(size=15,weight="bold",family="Helvetica")

            frm1=Frame(mwindow,height=630,width=200,bg="#FF33FF")
            frm1.grid(row=1,column=1,padx=10,pady=58,sticky= N)

            frm2=Frame(mwindow,height=630,width=660,bg="#FF33FF")
            frm2.grid(row=1,column=2,padx=10,sticky= W+N+S+E)
            image = Image.open("C:\\Users\\ASHISH KR. JHA\\Documents\\Desktop\\Python1\\pic\\" + str(cid) +".jpg")
            img1=image.resize((200,150),Image.ANTIALIAS)
            img1.save("C:\\Users\\ASHISH KR. JHA\\Documents\\Desktop\\Python1\\pic\\" + str(cid) +".gif")

           # image1 = PhotoImage(file="C:\\Users\\ASHISH KR. JHA\\Documents\\Desktop\\Python1\\pic\\" + str(cid) +".gif")
           # lbl_image = Label(frm1)
           # lbl_image["image"] = image1
            #lbl_image.grid(row=1, column=1,pady=5,sticky=(NW))

            if cid is not None:
                import mysql.connector 
                cnx = mysql.connector.connect(user='root', password='aashishgolu', host='127.0.0.1', database='project')
                if(cnx):
                    cursor=cnx.cursor()
                    try:
                        q= "select fname,mname,sname,eid,cid,email,contact,city,state,course,sem,stream from sregister where cid=%s"
                        d=(str(cid),)
                        cursor.execute(q,d)
                        row_pass=cursor.fetchone()

                        now=datetime.datetime.now()
                        cur_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
                        mydate=date.today()
                        cur_day=calendar.day_name[mydate.weekday()]

                        frm4=Frame(frm2,height=60,width=660,bg="#FF33FF")
                        frm4.grid(row=2,column=1,sticky=W)


                        lbl2=Label(frm4,text="First Name",fg="blue",bg="#FF33FF")
                        lbl2.grid(row=1,column=1,sticky=W,padx=20,pady=10)
                        lbl21=Label(frm4,text=str(row_pass[0]),fg="white",bg="#FF33FF")
                        lbl21.grid(row=1,column=2,sticky=W,padx=4,pady=2)
                        lbl3=Label(frm4,text="MIddle Name",fg="blue",bg="#FF33FF")
                        lbl3.grid(row=2,column=1,sticky=W,padx=20,pady=10)
                        lbl31=Label(frm4,text=str(row_pass[1]),fg="white",bg="#FF33FF")
                        lbl31.grid(row=2,column=2,sticky=W,padx=4,pady=2)
                        lbl4=Label(frm4,text="Last Name",fg="blue",bg="#FF33FF")
                        lbl4.grid(row=3,column=1,sticky=W,padx=20,pady=10)
                        lbl41=Label(frm4,text=str(row_pass[2]),fg="white",bg="#FF33FF")
                        lbl41.grid(row=3,column=2,sticky=W,padx=4,pady=2)
                        
                        lbl5=Label(frm4,text="Enrollment ID",fg="blue",bg="#FF33FF")
                        lbl5.grid(row=4,column=1,sticky=W,padx=20,pady=10)
                        lbl51=Label(frm4,text=str(row_pass[3]),fg="white",bg="#FF33FF")
                        lbl51.grid(row=4,column=2,sticky=W,padx=4,pady=2)
                        lblcid=Label(frm4,text="College ID",fg="blue",bg="#FF33FF")
                        lblcid.grid(row=5,column=1,sticky=W,padx=20,pady=10)
                        lblcid1=Label(frm4,text=str(row_pass[4]),fg="white",bg="#FF33FF")
                        lblcid1.grid(row=5,column=2,sticky=W,padx=4,pady=2)
                        lbl6=Label(frm4,text="Email",fg="blue",bg="#FF33FF")
                        lbl6.grid(row=6,column=1,sticky=W,padx=20,pady=10)
                        lbl61=Label(frm4,text=str(row_pass[5]),fg="white",bg="#FF33FF")
                        lbl61.grid(row=6,column=2,sticky=W,padx=4,pady=2)
                        lbl7=Label(frm4,text="Contact",fg="blue",bg="#FF33FF")
                        lbl7.grid(row=7,column=1,sticky=W,padx=20,pady=10)
                        lbl71=Label(frm4,text=str(row_pass[6]),fg="white",bg="#FF33FF")
                        lbl71.grid(row=7,column=2,sticky=W,padx=4,pady=2)
                        lblcity=Label(frm4,text="City",fg="blue",bg="#FF33FF")
                        lblcity.grid(row=8,column=1,sticky=W,padx=20,pady=10)
                        lblcity1=Label(frm4,text=str(row_pass[7]),fg="white",bg="#FF33FF")
                        lblcity1.grid(row=8,column=2,sticky=W,padx=4,pady=2)
                    
                        lblstate=Label(frm4,text="State",fg="blue",bg="#FF33FF")
                        lblstate.grid(row=9,column=1,sticky=W,padx=20,pady=10)
                        lblstate1=Label(frm4,text=str(row_pass[8]),fg="white",bg="#FF33FF")
                        lblstate1.grid(row=9,column=2,sticky=W,padx=4,pady=2)
                        course=Label(frm4,text="Courses",fg="blue",bg="#FF33FF")
                        course.grid(row=10,column=1,sticky=W,padx=20,pady=10)
                        course1=Label(frm4,text=str(row_pass[9]),fg="white",bg="#FF33FF")
                        course1.grid(row=10,column=2,sticky=W,padx=4,pady=2)
                        lblsem=Label(frm4,text="Semester",fg="blue",bg="#FF33FF")
                        lblsem.grid(row=11,column=1,sticky=W,padx=20,pady=10)
                        lblsem1=Label(frm4,text=str(row_pass[10]),fg="white",bg="#FF33FF")
                        lblsem1.grid(row=11,column=2,sticky=W,padx=4,pady=2)
                    
                        stream=Label(frm4,text="Stream",fg="blue",bg="#FF33FF")
                        stream.grid(row=12,column=1,sticky=W,padx=20,pady=10)

                        stream1=Label(frm4,text=str(row_pass[11]),fg="white",bg="#FF33FF")
                        stream1.grid(row=12,column=2,sticky=W,padx=4,pady=2)

                        cnx.commit()

                        cursor.close()
                        cnx.close()
                    except Exception as e:
                        import tkMessageBox
                        tkMessageBox.showwarning("Warning",str(e))
    except Exception as e:
        import tkMessageBox
        tkMessageBox.showwarning("Warning",str(e))   
                            



            

            
