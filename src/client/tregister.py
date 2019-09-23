import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
import ttk
import cv2
class TRegister:
    def __init__(self,mwindow):
        self.master=mwindow
        self.new(self.master)
    def new(self,caller):

        global masterr
        fname=StringVar();
        mname=StringVar();
        sname=StringVar();
        email=StringVar();
        contact=StringVar();
        h_no=StringVar();
        area=StringVar();
        city=StringVar();
        state=StringVar();
        course_name=StringVar();
        sem_name=StringVar();
        stream_name=StringVar();
        password=StringVar();
        password1=StringVar();
        def save():
            global fnam
            fnam=fname.get()
            mnam=mname.get()
            snam=sname.get()
            e_mail=email.get()
            contact_no=contact.get()
            house_no=h_no.get()
            area_name=area.get()
            city_name=city.get()
            state_name=state.get()
            course__name=course_name.get()
            sem__no=sem_name.get()
            stream_no=stream_name.get()
            password_2=password.get()
            password_1=password1.get()
            def invoke():
                
                flag=0
                cam = cv2.VideoCapture(0)
                while(True):
                    ret, img = cam.read()
                    if(cv2.imwrite("Photo/TPic/"+str(fnam)+str(contact_no)+".jpg", img)):
                        flag=1
                    else:
                        flag=0
                    cv2.imshow('frame',img)
                    if  cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                print("hello")
                cam.release()
                cv2.destroyAllWindows()
                if(flag==1):
                    print("hello")
                    import tkMessageBox
                    tkMessageBox.showwarning("Done","Thankyou Sir")
                    fname.set("")
                    mname.set("")
                    sname.set("")
                    email.set("")
                    contact.set("")
                    h_no.set("")
                    area.set("")
                    city.set("")
                    state.set("")
                    course_name.set("")
                    sem_name.set("")
                    stream_name.set("")
                    password.set("")
                    password1.set("")
                    lbl_image.grid_forget()
                    ibt.grid_forget()
                
            if(fnam=="" or snam=="" or e_mail=="" or city_name=="" or state_name==""
               or course__name=="" or sem__no == "" or password_1== "" or password_2 == "" or
               stream_no=="" or contact_no ==""):
                import tkMessageBox
                tkMessageBox.showwarning("OK","Fill (*) Mark Feild")
            else:
                
                if(password_2 != password_1):
                    
                    import tkMessageBox
                    tkMessageBox.showwarning("WARNING","Incorrect Paasword")
                else:
                    import datetime
                    now=datetime.datetime.now()
                    reg_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
                    reg_time=str(str(now.hour)+":"+str(now.minute)+":"+str(now.second))
                    import mysql.connector 
                    cnx = mysql.connector.connect(user='root', password='aashishgolu', host='127.0.0.1', database='project')
                    if(cnx):
                        cursor=cnx.cursor()
                        try:
                            q="select * from t_register where email=%s"
                            data=(str(e_mail),)
                            cursor.execute(q,data)
                            result=cursor.fetchone()
                            cnx.commit()
                            if(not result):
                                q= "insert into t_register  (fname,mname,sname,email,h_no,area,city,state,course,sem,password,regdate,regtime,stream,contact) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data= ( str(fnam) ,str(mnam) ,str(snam),str(e_mail) ,str(house_no) ,str(area_name),
                                        str(city_name) ,str(state_name) ,str(course__name) ,
                                        str(sem__no) ,str(password_2),str(reg_date) ,str(reg_time) ,str(stream_no) ,str(contact_no))
                                cursor.execute(q,data)
                                cnx.commit()
                                t=cursor.rowcount
                                if(int(cursor.rowcount)>=1):
                                    import tkMessageBox
                                    tkMessageBox.showinfo("Done","Registerd Successfully")

                                    image = Image.open("pic/fingerprint.jpg")
                                    img1=image.resize((200,150),Image.ANTIALIAS)
                                    img2=img1.save("pic/fingerprint_new.gif")

                                    image = PhotoImage(file="pic/fingerprint_new.gif")
                                    lbl_image = Label(frm1)
                                    lbl_image["image"] = image
                                    lbl_image.grid(row=1, column=1,pady=5,sticky=(NW))
                                    ibt=Button(frm1,width=10,text="Profile Pic",bg="gray",fg="#990066",command=invoke)
                                    ibt.grid(row=2,column=1,sticky= S)
                            else:
                                import tkMessageBox
                                tkMessageBox.showinfo("Error","You are already registered")
                                
                        except Exception as e:
                            print(str(type(e))+str(e))
                        cursor.close()
                    cnx.close() 

        
        masterr =Toplevel(caller)   
        
        masterr.title("FACULTY REGISTRATION")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")

        frm1=Frame(masterr,height=630,width=200,bg="#990066")
        frm1.grid(row=1,column=1,padx=10,pady=58,sticky= N)
##        image = Image.open("photo0.jpg")
##        img1=image.resize((200,150),Image.ANTIALIAS)
##        img2=img1.save("ad2.gif")
##
##        image = PhotoImage(file="ad2.gif")
##        lbl_image = Label(frm1)
##        lbl_image["image"] = image
##        lbl_image.grid(row=1, column=1,pady=5,sticky=(NW))
##
##        ibt=Button(frm1,width=15,text="Upload Photo",bg="gray",fg="#990066",command=invoke)
##        ibt.grid(row=2,column=1,sticky= S)

        frm2=Frame(masterr,height=630,width=660,bg="#990066")
        frm2.grid(row=1,column=2,padx=10,pady=10,sticky= W+N+S+E)

        frm3=Frame(frm2,height=60,width=660,bg="#990066")
        frm3.grid(row=1,column=1)

        lbl1=Label(frm3,font=f,text="FACULTY REGISTRATION",width=58,bg="#990066",fg="gray")
        lbl1.grid(row=1,column=1,padx=5,pady=5)

        f1=tkFont.Font(weight="bold",family="Helvetica")

        frm4=Frame(frm2,height=60,width=660,bg="#990066")
        frm4.grid(row=2,column=1,sticky=W)

        lblf=Label(frm4,text="First Name(*)",fg="gray",bg="#990066")
        lblf.grid(row=1,column=1,sticky=W,padx=4,pady=2)
        Entf=Entry(frm4,width=25,textvariable=fname)
        Entf.grid(row=2,column=1,sticky=W,padx=4,pady=2)
        lblm=Label(frm4,text="MIddle Name",fg="gray",bg="#990066")
        lblm.grid(row=1,column=2,sticky=W,padx=4,pady=2)
        Entm=Entry(frm4,width=25,textvariable=mname)
        Entm.grid(row=2,column=2,sticky=W,padx=4,pady=2)
        lbll=Label(frm4,text="Last Name(*)",fg="gray",bg="#990066")
        lbll.grid(row=1,column=3,sticky=W,padx=4,pady=2)
        Entl=Entry(frm4,width=25,textvariable=sname)
        Entl.grid(row=2,column=3,sticky=W,padx=4,pady=2)

        lblemail=Label(frm4,text="Email(*)",fg="gray",bg="#990066")
        lblemail.grid(row=3,column=1,sticky=W,padx=2,pady=2)
        Entemail=Entry(frm4,width=52,textvariable=email)
        Entemail.grid(row=4,column=1,columnspan=2,sticky=W,padx=2,pady=2)
        lblcont=Label(frm4,text="Contact(*)",fg="gray",bg="#990066")
        lblcont.grid(row=3,column=3,sticky=W,padx=2,pady=2)
        Entcont=Entry(frm4,width=25,textvariable=contact)
        Entcont.grid(row=4,column=3,sticky=W,padx=2,pady=2)
        lbladd=LabelFrame(frm4,text="Address",fg="gray",bg="#990066",width=50)
        lbladd.grid(row=5,column=1,columnspan=2,sticky=W,padx=2,pady=2)
        lblhome=Label(lbladd,text="House No",fg="gray",bg="#990066")
        lblhome.grid(row=1,column=1,sticky=W,padx=2,pady=2)
        Enthome=Entry(lbladd,width=25,textvariable=h_no)
        Enthome.grid(row=2,column=1,sticky=W,padx=2,pady=2)
        lblarea=Label(lbladd,text="Area/Landmark",fg="gray",bg="#990066")
        lblarea.grid(row=3,column=1,sticky=W,padx=2,pady=2)
        Entarea=Entry(lbladd,width=25,textvariable=area)
        Entarea.grid(row=4,column=1,sticky=W,padx=2,pady=2)
        lblcity=Label(lbladd,text="City(*)",fg="gray",bg="#990066")
        lblcity.grid(row=1,column=2,sticky=W,padx=2,pady=2)
        Entcity=Entry(lbladd,width=25,textvariable=city)
        Entcity.grid(row=2,column=2,sticky=W,padx=2,pady=2)
        lblstate=Label(lbladd,text="State(*)",fg="gray",bg="#990066")
        lblstate.grid(row=3,column=2,sticky=W,padx=2,pady=2)
        Entstate=Entry(lbladd,width=25,textvariable=state)
        Entstate.grid(row=4,column=2,sticky=W,padx=2,pady=2)

        course=Label(frm4,text="Courses(*)",fg="gray",bg="#990066")
        course.grid(row=6,column=1,sticky=W,padx=2,pady=2)
        courses = ttk.Combobox(frm4,state="readonly",textvariable=course_name,
        values = ('BTech', 'MTech'))
        courses.grid(row=7,column=1,sticky=W,padx=2,pady=2)
        lblsem=Label(frm4,text="Semester(*)",fg="gray",bg="#990066")
        lblsem.grid(row=6,column=2,sticky=W,padx=2,pady=2)
        sem= ttk.Combobox(frm4,state="readonly",textvariable=sem_name,
        values = ('SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4','SEMESTER 5','SEMESTER 6','SEMESTER 7','SEMESTER 8'))
        sem.grid(row=7,column=2,sticky=W,padx=2,pady=2)
        stream=Label(frm4,text="Stream(*)",fg="gray",bg="#990066")
        stream.grid(row=6,column=3,sticky=W,padx=2,pady=2)
        sub = ttk.Combobox(frm4,state="readonly",textvariable=stream_name,
        values = ('CS','CIVIL', 'IT', 'ECE','EIC','EE', 'ME'))
        sub.grid(row=7,column=3,sticky=W,padx=2,pady=2)

        lblpass=Label(frm4,text="Password(*)",fg="gray",bg="#990066")
        lblpass.grid(row=8,column=1,sticky=W,padx=2,pady=2)
        Entpass=Entry(frm4,width=25,textvariable=password,show="*")
        Entpass.grid(row=9,column=1,sticky=W,padx=2,pady=2)
        lblrepass=Label(frm4,text="Re-Enter Password(*)",fg="gray",bg="#990066")
        lblrepass.grid(row=8,column=2,sticky=W,padx=2,pady=2)
        Entrepass=Entry(frm4,width=25,textvariable=password1,show="*")
        Entrepass.grid(row=9,column=2,sticky=W,padx=2,pady=2)
        submit=Button(frm4,width=10,text="Save Details",bg="gray",fg="#990066",command=save)
        submit.grid(row=10,column=1,sticky=W,padx=2,pady=20)
        masterr.mainloop()
    

