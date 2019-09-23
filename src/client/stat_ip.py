from Tkinter import *
import tkFont
import PIL
from PIL import Image
import ttk
import socket
import datetime
from datetime import date
import calendar



class Att_Status_ip:
    def __init__(self,win,email):
        masterr=Toplevel(win)
        masterr.title("STUDENT Profile")
        masterr.configure(height=650,width=900,bg="#990066")
        masterr.minsize(height=650,width=900)
        masterr.maxsize(height=650,width=900)
        self.menu=Menu(masterr)
        masterr['menu']=self.menu
        self.menu1=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.menu1,label="Admin")
        self.menu1.add_command(label="System Guide")
        self.menu1.add_command(label="System Close")
        self.menu1.add_command(label="Change Password")
        self.menu.add_command(label="System Guide")
        self.menu.add_command(label="System Close")
        self.menu.add_command(label="Change Password")
        self.new2(masterr,email)
        self.help=Menu(self.menu,activebackground="pink",tearoff=0)
        self.menu.add_cascade(menu=self.help,label="help")
        self.help.add_command(label="About Us")
        masterr.mainloop()
    def new2(self,caller,email):
        course_name1=StringVar();
        sem_name1=StringVar();
        stream_name1=StringVar();
        def save2():
            
                    
                    
            now=datetime.datetime.now()
            course__name1=course_name1.get()
            sem__no1=sem_name1.get()
            stream_no1=stream_name1.get()
            if(course__name1!="" and sem__no1!="" and stream_no1!=""):
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = "192.168.43.67"
                port = 5000
                server.connect( (host, port) )
                name="Status"+"/"+str(course__name1)+"/"+str(sem__no1)+"/"+str(stream_no1)
                name=name.encode("utf-8")
                server.send(name)
                emp=""
                while True:
                    d=server.recv(16)
                    if not d:
                        break
                    d=d.decode("utf-8")
                    emp=emp+str(d)
                useful=emp.split("@@")
                use_det=useful[0]
                use_att=useful[1]
                students=use_det.split("//")
                attendance=use_att.split("/")
                
                    
                



                
                server.close()
                frm3=Frame(frm2,height=530,width=660,bg="#990066")
                frm3.grid(row=2,column=1,sticky= W+N+S+E,pady=10)
                def EmailSent(win,em_ail,q):
                    def open_email():
                        if(em_ail!=""):
                            strFrom = 'gecafacerecog@gmail.com'
                            strTo = str(em_ail)

                            from email.MIMEMultipart import MIMEMultipart
                            from email.MIMEText import MIMEText

                            msgRoot = MIMEMultipart('related')
                            msgRoot['Subject'] = 'Low Attendance'
                            msgRoot['From'] = strFrom
                            msgRoot['To'] = strTo

                            msgAlternative = MIMEMultipart('alternative')
                            msgRoot.attach(msgAlternative)

                            mailBody = "This is a warning letter regarding your low attendance.Improve your behaviour otherwise you have to face serious consequences."
                            msgText = MIMEText(mailBody, 'html')
                            msgAlternative.attach(msgText)


                            import smtplib
                            smtp = smtplib.SMTP('smtp.gmail.com:587')
                            smtp.ehlo()
                            smtp.starttls()
                            smtp.login('gecafacerecog@gmail.com', 'aaadni@!1213')
                            smtp.sendmail(strFrom, strTo, msgRoot.as_string())
                            if(smtp.quit()):
                                import tkMessageBox
                                tkMessageBox.showwarning("Warning","Email Sent")
                                
                    detailsem=Button(frm4,text="Send",width=10,fg="#990066",bg="gray",command=open_email)
                    detailsem.grid(row=q,column=6,sticky=W,padx=5)
                    
                def Butt(win,cid,p):
                    def open_det():
                        
                        if(cid!=""):
                            from inputd1 import inputdata
                            inputdata(win,cid).new1()
                        else:
                            import tkMessageBox
                            tkMessageBox.showwarning("Warning","No Data Received From Server")
                    
                    details=Button(frm4,text="Details",width=10,fg="#990066",bg="gray",command=open_det)
                    details.grid(row=p,column=5,sticky=W,padx=5)

                    
                i=0
                while(i<len(students)-1):
                    


                    name=students[i].split("/")
                    
                    
                    id_lbl1=Label(frm4,text=str(name[0]),width=25,fg="gray",bg="#990066")
                    id_lbl1.grid(row=i+2,column=1,sticky=W,padx=5,pady=5)

                    n_lbl1=Label(frm4,text=str(name[2]),width=10,fg="gray",bg="#990066")
                    n_lbl1.grid(row=i+2,column=2,sticky=W,padx=5,pady=5)
                    
                    val=(int(attendance[i][0])*100)/now.day

                    mark_lbl1=Label(frm4,text=str(val),width=10,fg="gray",bg="#990066")
                    mark_lbl1.grid(row=i+2,column=3,sticky=W,padx=5,pady=5)

                    if(val<75):
                        mark_lbl11=Label(frm4,text="Low Attendance",width=15,fg="gray",bg="#990066")
                        mark_lbl11.grid(row=i+2,column=4,sticky=W,padx=5,pady=5)
                    else:
                        mark_lbl11=Label(frm4,text="",width=10,fg="gray",bg="#990066")
                        mark_lbl11.grid(row=i+2,column=4,sticky=W,padx=5,pady=5)
                        

                    Butt(caller,name[2],i+2)
                    if(val<75):
                        EmailSent(caller,name[3],i+2)


                    i=i+1
                    
                    
                
                
            else:
                import tkMessageBox
                tkMessageBox.showwarning("Warning"," (*) Feild Required")

                
        f=tkFont.Font(size=15,weight="bold",family="Helvetica")

        frm1=Frame(caller,height=630,width=200,bg="#990066")
        frm1.grid(row=1,column=1,padx=10,pady=58,sticky= N)

        frm2=Frame(caller,height=630,width=660,bg="#990066")
        frm2.grid(row=1,column=2,padx=10,sticky= W+N+S+E)


        
        course=Label(frm1,text="Courses(*)",fg="gray",bg="#990066",font=f)
        course.grid(row=1,column=1,sticky=W,padx=2,pady=2)
        courses = ttk.Combobox(frm1,state="readonly",textvariable=course_name1,
        values = ('BTech', 'MTech'))
        courses.grid(row=2,column=1,sticky=W,padx=2,pady=2)
        lblsem=Label(frm1,text="Semester(*)",fg="gray",bg="#990066",font=f)
        lblsem.grid(row=3,column=1,sticky=W,padx=2,pady=2)
        sem= ttk.Combobox(frm1,state="readonly",textvariable=sem_name1,
        values = ('SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4','SEMESTER 5','SEMESTER 6','SEMESTER 7','SEMESTER 8'))
        sem.grid(row=4,column=1,sticky=W,padx=2,pady=2)
        stream=Label(frm1,text="Stream(*)",fg="gray",bg="#990066",font=f)
        stream.grid(row=5,column=1,sticky=W,padx=2,pady=2)
        sub = ttk.Combobox(frm1,state="readonly",textvariable=stream_name1,
        values = ('CS','CIVIL', 'IT', 'ECE','EIC','EE', 'ME'))
        sub.grid(row=6,column=1,sticky=W,padx=2,pady=2)
        submit=Button(frm1,width=10,text="View Status",bg="gray",fg="#990066",command=save2)
        submit.grid(row=7,column=1,sticky=W,padx=30,pady=20)

        frm4=Frame(frm2,width=660,bg="#990066")
        frm4.grid(row=1,column=1,sticky= W+N+S+E)

        id_lbl=Label(frm4,text="Name",width=20,fg="gray",bg="#990066")
        id_lbl.grid(row=1,column=1,sticky=W,padx=5)

        n_lbl=Label(frm4,text="College ID",width=10,fg="gray",bg="#990066")
        n_lbl.grid(row=1,column=2,sticky=W,padx=5)

        mark_lbl=Label(frm4,text="Attendance(%)",width=15,fg="gray",bg="#990066")
        mark_lbl.grid(row=1,column=3,sticky=W,padx=5)

        mark_lbl1=Label(frm4,text="Status",width=10,fg="gray",bg="#990066")
        mark_lbl1.grid(row=1,column=4,sticky=W,padx=5)

        details=Label(frm4,text="Details",width=10,fg="gray",bg="#990066")
        details.grid(row=1,column=5,sticky=W,padx=5)

        details1=Label(frm4,text="Send Email",width=10,fg="gray",bg="#990066")
        details1.grid(row=1,column=6,sticky=W,padx=5)

        
