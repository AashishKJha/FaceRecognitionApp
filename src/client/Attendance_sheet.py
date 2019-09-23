import Tkinter
from Tkinter import *
import tkFont
import ttk
import datetime
from datetime import date
import calendar
class attendance:
    try:
        def __init__(self,mwindow,e_mail,pass_word):
            self.new(mwindow,e_mail,pass_word)
        def new(self,mwindow,e_mail,pass_word):
            course_name=StringVar()
            stream_name=StringVar()
            sem_name=StringVar()

            def save():
                frm3=Frame(frm2,height=530,width=660,bg="#FF33FF")
                frm3.grid(row=2,column=1,sticky= W+N+S+E,pady=10)
                branch=stream_name.get()
                semester=sem_name.get()
                course__name=course_name.get()
                if(branch=="" or semester=="" or course__name==""):
                    import tkMessageBox
                    tkMessageBox.showwarning("Warning","(*) Feild Required")
                else:
                    def details(k,kid):
                        print("details_method")
                        def det_ail():
                            print("import")
                            from details1 import Detailsstudent
                            Detailsstudent(mwindow,kid)
##                        de_tails=Button(frm3,width=10,text="Veiw Details",bg="blue",fg="white",command=det_ail)
##                        de_tails.grid(row=k,column=4,sticky=E+W+N+S,padx=20)
                    def invoke(k,cid):
                        def go_db():
                            val=check1.get()
                            if(int(val)==1):
                                print("yes")
                                
                        check1=IntVar()
                        out3=Checkbutton(frm3,command=go_db,variable=check1,onvalue=1,offvalue=0,width=20,bg="#FF33FF")
                        out3.grid(row=k,column=3,sticky=W,padx=2)
                    
                            stream_name.set("")
                            sem_name.set("")
                            course_name.set("")
                            row_pass=""
                            
                            
                            
            
                        except Exception as e:
                            import tkMessageBox
                            tkMessageBox.showwarning("Warning",str(e))

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

            now=datetime.datetime.now()
            cur_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
            mydate=date.today()
            cur_day=calendar.day_name[mydate.weekday()]

            date_lbl=Label(frm1,text="DATE : "+str(cur_date),fg="blue",bg="#FF33FF")
            date_lbl.grid(row=1,column=1,sticky=W,padx=2,pady=10)

            day_lbl=Label(frm1,text="DAY : "+str(cur_day),fg="blue",bg="#FF33FF")
            day_lbl.grid(row=2,column=1,sticky=W,padx=2,pady=10)

            

            course=Label(frm1,text="Courses(*)",fg="blue",bg="#FF33FF")
            course.grid(row=3,column=1,sticky=W,padx=2,pady=10)
            courses = ttk.Combobox(frm1,state="readonly",textvariable=course_name,
            values = ('BTech', 'MTech'))
            courses.grid(row=4,column=1,sticky=W,padx=2,pady=2)

            stream=Label(frm1,text="Stream(*)",fg="blue",bg="#FF33FF")
            stream.grid(row=5,column=1,sticky=W,padx=2,pady=10)
            sub = ttk.Combobox(frm1,state="readonly",textvariable=stream_name,
            values = ('CS','CIVIL', 'IT', 'ECE','EIC','EE', 'ME'))
            sub.grid(row=6,column=1,sticky=W,padx=2,pady=2)
            
            lblsem=Label(frm1,text="Semester(*)",fg="blue",bg="#FF33FF")
            lblsem.grid(row=7,column=1,sticky=W,padx=2,pady=10)
            sem= ttk.Combobox(frm1,state="readonly",textvariable=sem_name,
            values = ('SEMESTER 1', 'SEMESTER 2', 'SEMESTER 3', 'SEMESTER 4','SEMESTER 5','SEMESTER 6','SEMESTER 7','SEMESTER 8'))
            sem.grid(row=8,column=1,sticky=W,padx=2,pady=2)

            submit=Button(frm1,width=10,text="Save Details",bg="blue",fg="white",command=save)
            submit.grid(row=9,column=1,sticky=W,padx=2,pady=20)

            frm4=Frame(frm2,width=660,bg="#FF33FF")
            frm4.grid(row=1,column=1,sticky= W+N+S+E)

            id_lbl=Label(frm4,text="Name",width=20,fg="blue",bg="#FF33FF")
            id_lbl.grid(row=1,column=1,sticky=W,padx=2)

            n_lbl=Label(frm4,text="College ID",width=20,fg="blue",bg="#FF33FF")
            n_lbl.grid(row=1,column=2,sticky=W,padx=2)

            mark_lbl=Label(frm4,text="Attendance(%)",width=20,fg="blue",bg="#FF33FF")
            mark_lbl.grid(row=1,column=3,sticky=W,padx=2)

            details=Label(frm4,text="Details",width=20,fg="blue",bg="#FF33FF")
            details.grid(row=1,column=4,sticky=W,padx=2)
            
            
            
            print(e_mail)
            print(pass_word)
            mwindow.mainloop()
    except Exception as e:
        print(str(e))
w=Tk()
attendance(w,"aashishjha.1994@gmail.com","111")
