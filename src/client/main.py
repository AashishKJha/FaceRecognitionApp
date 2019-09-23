import Tkinter
from Tkinter import *
import tkFont
class mainwindow:
    try:
        def __init__(self,win,email):
            self.win=win
            self.email=email
            self.mwindow=Toplevel(win)
            self.mwindow.title("ATTENDANCE SYSTEM")
            self.mwindow.configure(height=650,width=900,bg="#990066")
            self.mwindow.minsize(height=650,width=900)
            self.mwindow.maxsize(height=650,width=900)
            self.menu=Menu(self.mwindow)
            self.mwindow['menu']=self.menu
            self.menu1=Menu(self.menu,activebackground="#990066",tearoff=0)
            self.menu.add_cascade(menu=self.menu1,label="User")
            self.menu1.add_command(label="System Guide")
            self.menu1.add_command(label="System Close")
            self.help=Menu(self.menu,activebackground="#990066",tearoff=0)
            self.menu.add_cascade(menu=self.help,label="Help")
            self.help.add_command(label="About Us")
            f=tkFont.Font(size=10,weight="bold",family="Helvetica")
            
        
            
            self.lbl1=Frame(self.mwindow,height=100,width=200,bg="pink")
            self.lbl1.grid(row=1,column=1,padx=300,pady=250,sticky=N+W+S+E)
            self.bt1=Button(self.lbl1,text="MARK ATTENDANCE",height=4,width=20,bg="gray",fg="#990066",command=self.mattendance,font=f)
            self.bt1.grid(row=1,column=1,sticky='nswe')
            
            self.bt2=Button(self.lbl1,text="MONTHLY STATUS",height=4,width=20,bg="gray",fg="#990066",command=self.status,font=f)
            self.bt2.grid(row=1,column=2)
            
##            self.lbl3=Frame(self.mwindow,height=100,width=200,bg="pink")
##            self.lbl3.grid(row=2,column=1,sticky=N+W+S+E)
            self.bt3=Button(self.lbl1,text="STUDENTS PROFILE",height=4,width=20,bg="gray",fg="#990066",command=self.sprofile,font=f)
            self.bt3.grid(row=2,column=1)
            
##            self.lbl4=Frame(self.mwindow,height=100,width=200,bg="pink")
##            self.lbl4.grid(row=2,column=2,sticky=N+W+S+E)
            self.bt4=Button(self.lbl1,text="EXIT SYSTEM",height=4,width=20,bg="gray",fg="#990066",command=self.EXIT,font=f)
            self.bt4.grid(row=2,column=2,sticky='nswe')
            self.mwindow['menu']=self.menu
            
            self.mwindow.mainloop()
        def sprofile(self):
            self.mwindow.state(newstate="iconic")
            from inputd import inputdata
            inputdata(self.mwindow)
            
        def mattendance(self):
            self.mwindow.state(newstate="iconic")
            from cleint import LoginAccepted
            LoginAccepted(self.mwindow,self.email)
        def status(self):
            self.mwindow.state(newstate="iconic")
            from stat_ip import Att_Status_ip
            Att_Status_ip(self.mwindow,self.email)
        def EXIT(self):
            self.win.destroy()
        
    except Exception as e:
        import tkMessageBox
        tkMessageBox.showwarning("Warning",str(e))
