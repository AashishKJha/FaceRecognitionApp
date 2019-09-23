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
                                    
            
            
            fnam=fname.get()
            mnam=mname.get()
            snam=sname.get()
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
            if(fnam=="" or snam=="" or area_name=="" or e_mail=="" or city_name=="" or state_name==""
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
                            q2=("select * from t_register where email=%s")
                            data2=(str(e_mail),)
                            cursor.execute(q2,data2)
                            r=cursor.fetchone()
                            cnx.commit()
                            if(r):
                                import tkMessageBox
                                tkMessageBox.showinfo("OK","Already Exist")
                            else:
                                q= "insert into t_register  (fname,mname,sname,email,h_no,area,city,state,course,sem,password,regdate,regtime,stream,contact) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                data= ( str(fnam.upper()) ,str(mnam.upper()) ,str(snam.upper()),str(e_mail) ,str(house_no) ,str(area_name.upper()),
                                        str(city_name.upper()) ,str(state_name.upper()) ,str(course__name) ,
                                        str(sem__no) ,str(password_2),str(reg_date) ,str(reg_time) ,str(stream_no) ,str(contact_no))
                                cursor.execute(q,data)
                                cnx.commit()
                                t=cursor.rowcount
                                
                                if(int(t)>=1):
                                    import tkMessageBox
                                    tkMessageBox.showinfo("OK","Registerd Successfully")
                                    caller.destroy()
                                    
                                    
                                    
                                    
                        except Exception as e:
                            print(str(type(e))+str(e))
                        cursor.close()
                        cnx.close()
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

                

        masterr =Toplevel(caller)   
        masterr.title("FACULTY REGISTRATION")
        masterr.configure(height=500,width=600,bg="#990066")
        masterr.minsize(height=500,width=600)
        masterr.maxsize(height=500,width=600)

        f=tkFont.Font(size=15,weight="bold",family="Helvetica")
        frm2=Frame(masterr,height=500,width=550,bg="#990066")
        frm2.grid(row=1,column=1,padx=0,pady=10,sticky= W+N+S+E)

        frm3=Frame(frm2,height=60,width=550,bg="#990066")
        frm3.grid(row=1,column=1)

        lbl1=Label(frm3,font=f,text="FACULTY REGISTRATION",width=58,bg="#990066",fg="gray")
        lbl1.grid(row=1,column=1,padx=5,pady=5)

        f1=tkFont.Font(weight="bold",family="Helvetica")

        frm4=Frame(frm2,height=500,width=550,bg="#990066")
        frm4.grid(row=2,column=1,sticky=W,padx=50)

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
        
    
