import Tkinter
from Tkinter import *
import tkFont
import PIL
from PIL import Image
import ttk
class Register:
    def __init__(self,mwindow):
        self.master=mwindow
        self.new(self.master)
    def new(self,caller):
        
            
        
        global masterr
        fname=StringVar();
        mname=StringVar();
        sname=StringVar();
        eid=StringVar();
        cid=StringVar();
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
            def call(frm1):
                def invoke():
            
                    from  datasetCreator import datasetcreat
                    datasetcreat(c_id,course__name,sem__no,stream_no)
                    caller.state(newstate="iconic")
                def invoke1():
                    from UpperBodyCut import UpperBody
                    UpperBody(c_id,course__name,sem__no,stream_no)
                    caller.state(newstate="iconic")
                    lbl_image.grid_forget()
                    lbl_image1.grid_forget()
                    
                    ibt.grid_forget()
                    ibt1.grid_forget()
                image = Image.open("pic/fingerprint.jpg")
                img1=image.resize((200,150),Image.ANTIALIAS)
                img2=img1.save("pic/fingerprint_new.gif")

                image = PhotoImage(file="pic/fingerprint_new.gif")
                lbl_image = Label(frm1)
                lbl_image["image"] = image
                lbl_image.grid(row=1, column=1,pady=5,sticky=(NW))
                ibt=Button(frm1,width=10,text="Scan",bg="blue",fg="white",command=invoke)
                ibt.grid(row=2,column=1,sticky= S)

                image1 = Image.open("fingerprint.jpg")
                img3=image1.resize((200,150),Image.ANTIALIAS)
                img4=img3.save("ad3.gif")

                image1 = PhotoImage(file="ad3.gif")
                lbl_image1 = Label(frm1)
                lbl_image1["image"] = image1
                lbl_image1.grid(row=3, column=1,pady=4,sticky=(NW))
                ibt1=Button(frm1,width=10,text="Profile",bg="blue",fg="white",command=invoke1)
                ibt1.grid(row=4,column=1,sticky= S)
                                    
            
            
            fnam=fname.get()
            mnam=mname.get()
            snam=sname.get()
            en_id=eid.get()
            global c_id
            c_id=cid.get()
            e_mail=email.get()
            contact_no=contact.get()
            house_no=h_no.get()
            area_name=area.get()
            city_name=city.get()
            state_name=state.get()
            global course__name
            course__name=course_name.get()
            global sem__no
            sem__no=sem_name.get()
            global stream_no
            stream_no=stream_name.get()
            password_2=password.get()
            password_1=password1.get()
            if(fnam=="" or snam=="" or en_id=="" or c_id=="" or area_name=="" or e_mail=="" or city_name=="" or state_name==""
               or course__name=="" or sem__no == "" or password_1== "" or password_2 == "" or
               stream_no=="" or contact_no ==""):
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")
            else:
                
            
                if(password_2 != password_1):
                    import tkMessageBox
                    tkMessageBox.showwarning("WARNING","Incorrect Password")
                else:
                    import datetime
                    now=datetime.datetime.now()
                    reg_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
                    reg_time=str(str(now.hour)+":"+str(now.minute)+":"+str(now.second))
                    import mysql.connector 
                    cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
                    if(cnx):
                        cursor=cnx.cursor()
                        try:
                            q2=("select * from sregister where email=%s")
                            data2=(str(e_mail),)
                            cursor.execute(q2,data2)
                            r=cursor.fetchone()
                            cnx.commit()
                            if(r):
                                import tkMessageBox
                                tkMessageBox.showinfo("OK","Already Exist")
                            else:
                                q= "insert into sregister  (fname,mname,sname,eid,cid,email,h_no,area,city,state,course,sem,password,regdate,regtime,stream,contact) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data= ( str(fnam.upper()) ,str(mnam.upper()) ,str(snam.upper()) ,str(en_id.upper()) ,
                                        str(c_id.upper()) ,str(e_mail) ,str(house_no) ,str(area_name.upper()),
                                        str(city_name.upper()) ,str(state_name.upper()) ,str(course__name) ,
                                        str(sem__no) ,str(password_2),str(reg_date) ,str(reg_time) ,str(stream_no) ,str(contact_no))
                                cursor.execute(q,data)
                                cnx.commit()
                                t=cursor.rowcount
                                q1="insert into attendance_m (cid,mark) VALUES (%s,%s)"
                                data1=(str(c_id.upper()),int(0))
                                cursor.execute(q1,data1)
                                cnx.commit()
                                t1=cursor.rowcount
                                
                                if(int(t)>=1 and int(t1)>=1):
                                    import tkMessageBox
                                    tkMessageBox.showinfo("OK","Registerd Successfully")
                                    call(frm1)
                                    
                                    
                                    
                                    
                        except Exception as e:
                            print(str(type(e))+str(e))
                        cursor.close()
                        cnx.close()
                        fname.set("")
                        mname.set("")
                        sname.set("")
                        eid.set("")
                        cid.set("")
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

                

        masterr =Toplevel(caller)   
        masterr.title("STUDENT REGISTRATION")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")

        frm1=Frame(masterr,height=630,width=200,bg="#990066")
        frm1.grid(row=1,column=1,padx=10,pady=58,sticky= N)


        

        

##        image1 = Image.open("fingerprint.jpg")
##        img3=image1.resize((200,150),Image.ANTIALIAS)
##        img4=img3.save("ad3.gif")
##
##        image1 = PhotoImage(file="ad3.gif")
##        lbl_image1 = Label(frm1)
##        lbl_image1["image"] = image1
##        lbl_image1.grid(row=3, column=1,pady=4,sticky=(NW))

        frm2=Frame(masterr,height=630,width=660,bg="#990066")
        frm2.grid(row=1,column=2,padx=10,pady=10,sticky= W+N+S+E)

        frm3=Frame(frm2,height=60,width=660,bg="#990066")
        frm3.grid(row=1,column=1)

        lbl1=Label(frm3,font=f,text="STUDENT REGISTRATION",width=58,bg="#990066",fg="gray")
        lbl1.grid(row=1,column=1,padx=5,pady=5)

        f1=tkFont.Font(weight="bold",family="Helvetica")

        frm4=Frame(frm2,height=60,width=660,bg="#990066")
        frm4.grid(row=2,column=1,sticky=W)

        lbl2=Label(frm4,text="First Name(*)",fg="gray",bg="#990066")
        lbl2.grid(row=1,column=1,sticky=W,padx=4,pady=2)
        Ent1=Entry(frm4,width=25,textvariable=fname)
        Ent1.grid(row=2,column=1,sticky=W,padx=4,pady=2)
        lbl3=Label(frm4,text="MIddle Name",fg="gray",bg="#990066")
        lbl3.grid(row=1,column=2,sticky=W,padx=4,pady=2)
        Ent2=Entry(frm4,width=25,textvariable=mname)
        Ent2.grid(row=2,column=2,sticky=W,padx=4,pady=2)
        lbl4=Label(frm4,text="Last Name(*)",fg="gray",bg="#990066")
        lbl4.grid(row=1,column=3,sticky=W,padx=4,pady=2)
        Ent3=Entry(frm4,width=25,textvariable=sname)
        Ent3.grid(row=2,column=3,sticky=W,padx=4,pady=2)
        lbl5=Label(frm4,text="Enrollment ID(*)",fg="gray",bg="#990066")
        lbl5.grid(row=7,column=1,sticky=W,padx=2,pady=2)
        Ent4=Entry(frm4,width=25,textvariable=eid)
        Ent4.grid(row=8,column=1,sticky=W,padx=2,pady=2)
        lblcid=Label(frm4,text="College ID(*)",fg="gray",bg="#990066")
        lblcid.grid(row=7,column=2,sticky=W,padx=2,pady=2)
        Entcid=Entry(frm4,width=25,textvariable=cid)
        Entcid.grid(row=8,column=2,sticky=W,padx=2,pady=2)
        lbl6=Label(frm4,text="Email(*)",fg="gray",bg="#990066")
        lbl6.grid(row=9,column=1,sticky=W,padx=2,pady=2)
        Ent5=Entry(frm4,width=52,textvariable=email)
        Ent5.grid(row=10,column=1,columnspan=2,sticky=W,padx=2,pady=2)
        lbl7=Label(frm4,text="Contact(*)",fg="gray",bg="#990066")
        lbl7.grid(row=9,column=3,sticky=W,padx=2,pady=2)
        Ent5=Entry(frm4,width=25,textvariable=contact)
        Ent5.grid(row=10,column=3,sticky=W,padx=2,pady=2)
        lbl6=LabelFrame(frm4,text="Address",fg="gray",bg="#990066",width=50)
        lbl6.grid(row=13,column=1,columnspan=2,sticky=W,padx=2,pady=2)
        lblhome=Label(lbl6,text="House No",fg="gray",bg="#990066")
        lblhome.grid(row=1,column=1,sticky=W,padx=2,pady=2)
        Enthome=Entry(lbl6,width=25,textvariable=h_no)
        Enthome.grid(row=2,column=1,sticky=W,padx=2,pady=2)
        lblarea=Label(lbl6,text="Area/Landmark(*)",fg="gray",bg="#990066")
        lblarea.grid(row=3,column=1,sticky=W,padx=2,pady=2)
        Entarea=Entry(lbl6,width=25,textvariable=area)
        Entarea.grid(row=4,column=1,sticky=W,padx=2,pady=2)
        lblcity=Label(lbl6,text="City(*)",fg="gray",bg="#990066")
        lblcity.grid(row=1,column=2,sticky=W,padx=2,pady=2)
        Entcity=Entry(lbl6,width=25,textvariable=city)
        Entcity.grid(row=2,column=2,sticky=W,padx=2,pady=2)
        lblstate=Label(lbl6,text="State(*)",fg="gray",bg="#990066")
        lblstate.grid(row=3,column=2,sticky=W,padx=2,pady=2)
        Entstate=Entry(lbl6,width=25,textvariable=state)
        Entstate.grid(row=4,column=2,sticky=W,padx=2,pady=2)
        course=Label(frm4,text="Courses(*)",fg="gray",bg="#990066")
        course.grid(row=14,column=1,sticky=W,padx=2,pady=2)
        courses = ttk.Combobox(frm4,state="readonly",textvariable=course_name,
        values = ('BTech', 'MTech'))
        courses.grid(row=16,column=1,sticky=W,padx=2,pady=2)
        lblsem=Label(frm4,text="Semester(*)",fg="gray",bg="#990066")
        lblsem.grid(row=14,column=2,sticky=W,padx=2,pady=2)
        sem= ttk.Combobox(frm4,state="readonly",textvariable=sem_name,
        values = ('SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4','SEMESTER 5','SEMESTER 6','SEMESTER 7','SEMESTER 8'))
        sem.grid(row=16,column=2,sticky=W,padx=2,pady=2)
        stream=Label(frm4,text="Stream(*)",fg="gray",bg="#990066")
        stream.grid(row=14,column=3,sticky=W,padx=2,pady=2)
        sub = ttk.Combobox(frm4,state="readonly",textvariable=stream_name,
        values = ('CS','CIVIL', 'IT', 'ECE','EIC','EE', 'ME'))
        sub.grid(row=16,column=3,sticky=W,padx=2,pady=2)


        lbl7=Label(frm4,text="Password(*)",fg="gray",bg="#990066")
        lbl7.grid(row=17,column=1,sticky=W,padx=2,pady=2)
        Ent6=Entry(frm4,width=25,textvariable=password,show="*")
        Ent6.grid(row=18,column=1,sticky=W,padx=2,pady=2)
        lbl6=Label(frm4,text="Re-Enter Password(*)",fg="gray",bg="#990066")
        lbl6.grid(row=17,column=2,sticky=W,padx=2,pady=2)
        Ent5=Entry(frm4,width=25,textvariable=password1,show="*")
        Ent5.grid(row=18,column=2,sticky=W,padx=2,pady=2)
        
        submit=Button(frm4,width=10,text="Save Details",bg="gray",fg="#990066",command=save)
        submit.grid(row=19,column=1,sticky=W,padx=2,pady=20)
        masterr.mainloop()
        
    
