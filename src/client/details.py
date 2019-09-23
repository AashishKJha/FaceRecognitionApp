import Tkinter
from Tkinter import *
import tkFont
import ttk
import datetime
from datetime import date
import calendar
from PIL import Image
class Detailsstudent:
    try:
        def __init__(self,caller,data):
            self.new(caller,data)
        def new(self,caller,data):
            mwindow=Toplevel(caller)
            mwindow.title("ATTENDANCE SHEET")
            mwindow.configure(height=650,width=900,bg="#990066")
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

            frm1=Frame(mwindow,height=630,width=200,bg="#990066")
            frm1.grid(row=1,column=1,padx=10,pady=10,sticky= N)

            frm2=Frame(mwindow,height=630,width=660,bg="#990066")
            frm2.grid(row=1,column=2,padx=10,sticky= W+N+S+E)
            image = Image.open("Photo/Spic/"+str(data[2])+".jpg")
            img1=image.resize((200,150),Image.ANTIALIAS)
            img2=img1.save("pic/"+str(data[2])+".gif")

            image = PhotoImage(file="pic/"+str(data[2])+".gif")
            lbl_image = Label(frm1)
            lbl_image["image"] = image
            lbl_image.grid(row=1, column=1,pady=5,sticky=(NW))

            if data is not None:
                try:
                    frm4=Frame(frm2,height=60,width=660,bg="#990066")
                    frm4.grid(row=2,column=1,padx=10,pady=10,sticky=W)


                    lbl2=Label(frm4,text="Name",fg="gray",bg="#990066",font=f)
                    lbl2.grid(row=1,column=1,sticky=W,padx=4,pady=5)
                    lbl21=Label(frm4,text=str(data[0]),fg="gray",bg="#990066",font=f)
                    lbl21.grid(row=1,column=2,sticky=W,padx=50,pady=5)
                    lbl5=Label(frm4,text="Enrollment ID",fg="gray",bg="#990066",font=f)
                    lbl5.grid(row=2,column=1,sticky=W,padx=2,pady=5)
                    lbl51=Label(frm4,text=str(data[1]),fg="gray",bg="#990066",font=f)
                    lbl51.grid(row=2,column=2,sticky=W,padx=50,pady=5)
                    lblcid=Label(frm4,text="College ID",fg="gray",bg="#990066",font=f)
                    lblcid.grid(row=3,column=1,sticky=W,padx=2,pady=5)
                    lblcid1=Label(frm4,text=str(data[2]),fg="gray",bg="#990066",font=f)
                    lblcid1.grid(row=3,column=2,sticky=W,padx=50,pady=5)
                    lbl6=Label(frm4,text="Email",fg="gray",bg="#990066",font=f)
                    lbl6.grid(row=4,column=1,sticky=W,padx=2,pady=5)
                    lbl61=Label(frm4,text=str(data[3]),fg="gray",bg="#990066",font=f)
                    lbl61.grid(row=4,column=2,sticky=W,padx=50,pady=5)
                    lbl7=Label(frm4,text="House Address",fg="gray",bg="#990066",font=f)
                    lbl7.grid(row=5,column=1,sticky=W,padx=2,pady=5)
                    lbl71=Label(frm4,text=str(data[4]),fg="gray",bg="#990066",font=f)
                    lbl71.grid(row=5,column=2,sticky=W,padx=50,pady=5)
                    lblcity=Label(frm4,text="Area",fg="gray",bg="#990066",font=f)
                    lblcity.grid(row=6,column=1,sticky=W,padx=2,pady=5)
                    lblcity1=Label(frm4,text=str(data[5]),fg="gray",bg="#990066",font=f)
                    lblcity1.grid(row=6,column=2,sticky=W,padx=50,pady=5)
                
                    lblstate=Label(frm4,text="City",fg="gray",bg="#990066",font=f)
                    lblstate.grid(row=7,column=1,sticky=W,padx=2,pady=5)
                    lblstate1=Label(frm4,text=str(data[6]),fg="gray",bg="#990066",font=f)
                    lblstate1.grid(row=7,column=2,sticky=W,padx=50,pady=5)
                    course=Label(frm4,text="State",fg="gray",bg="#990066",font=f)
                    course.grid(row=8,column=1,sticky=W,padx=2,pady=5)
                    course1=Label(frm4,text=str(data[7]),fg="gray",bg="#990066",font=f)
                    course1.grid(row=8,column=2,sticky=W,padx=50,pady=5)
                    lblsem=Label(frm4,text="Course",fg="gray",bg="#990066",font=f)
                    lblsem.grid(row=9,column=1,sticky=W,padx=2,pady=5)
                    lblsem1=Label(frm4,text=str(data[8]),fg="gray",bg="#990066",font=f)
                    lblsem1.grid(row=9,column=2,sticky=W,padx=50,pady=5)
                    streamx=Label(frm4,text="Semester",fg="gray",bg="#990066",font=f)
                    streamx.grid(row=10,column=1,sticky=W,padx=2,pady=5)
                    streamy=Label(frm4,text=str(data[9]),fg="gray",bg="#990066",font=f)
                    streamy.grid(row=10,column=2,sticky=W,padx=50,pady=5)
                
                    stream=Label(frm4,text="Stream",fg="gray",bg="#990066",font=f)
                    stream.grid(row=11,column=1,sticky=W,padx=2,pady=5)

                    stream1=Label(frm4,text=str(data[10]),fg="gray",bg="#990066",font=f)
                    stream1.grid(row=11,column=2,sticky=W,padx=50,pady=5)
                    stream=Label(frm4,text="Mobile Number",fg="gray",bg="#990066",font=f)
                    stream.grid(row=12,column=1,sticky=W,padx=2,pady=5)

                    stream1=Label(frm4,text=str(data[11]),fg="gray",bg="#990066",font=f)
                    stream1.grid(row=12,column=2,sticky=W,padx=50,pady=5)
                    
                    mwindow.mainloop()
                except Exception as e:
                    import tkMessageBox
                    tkMessageBox.showwarning("Warning",str(e))
    except Exception as e:
        import tkMessageBox
        tkMessageBox.showwarning("Warning",str(e))                            



            

            
