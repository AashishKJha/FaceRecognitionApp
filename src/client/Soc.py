import socket
import Tkinter
from Tkinter import *
import tkFont
import ttk
import datetime
from datetime import date
import calendar

class Sock:
    def __init__(self,caller,course,stream,sem):
        
        self.output(caller,course,stream,sem)

    def output(self,caller,course,stream,sem):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        host = "192.168.43.67"
        port = 5000
        s.connect( (host, port) )

        name="Request/0"
        client_data=name.encode("utf-8")
        s.send(client_data)

        client_d1=s.recv(128)
        p=client_d1.decode("utf-8")
        
        if(int(p)==1):
            client_d=s.recv(16384)
            x=client_d.decode("utf-8")
            x=x+" "

            x=x.split("@@")
            s.close()


            wanted=x[0]
            y=wanted.split("@")
            marked=y[0]
            marked=marked+" "
            not_marked=y[1]
            not_marked=not_marked+" "
            stud=marked.split("//")
            not_stud=not_marked.split("//")
            
            name_att=[]
            roll_att=[]

            name_att1=[]
            roll_att1=[]

            i=0

            while(i<len(stud)-1):
                var=stud[i].split("/")
                name_att.append(var[0])
                roll_att.append(var[1])

                i=i+1

            j=0
            
            while(j<len(not_stud)-1):
                var1=not_stud[j].split("/")
                name_att1.append(var1[0])
                roll_att1.append(var1[1])

                j=j+1

            not_mark_att=[]
            def invoke(k,cid):
                check1=IntVar()
                
                def go_db():
                    val=check1.get()
                    if(int(val)==1):
                        not_mark_att.append(cid)
                        
                    
                
                out3=Checkbutton(frm2,command=go_db,width=5,variable=check1,onvalue=1,offvalue=0,bg="#990066")
                out3.grid(row=k+2,column=3,sticky=W,padx=30,pady=5)
            def save():
                i=0
                emp=""
                while(i<len(not_mark_att)):
                    emp=emp+not_mark_att[i]+"/"
                    i=i+1
                emp=emp+"@@"
                ##Server Connectivity
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                host = "192.168.43.67"
                port = 5000
                s.connect( (host, port) )

                name="End/0"
                client_data=name.encode("utf-8")
                s.send(client_data)

                client_d1=s.recv(128)
                p1=client_d1.decode("utf-8")
                if(int(p1)==1):
                    client_data=emp.encode("utf-8")
                    if(s.send(client_data)):
                        import tkMessageBox
                        tkMessageBox.showwarning("Thankyou","Data Sent Successfully")
                    
                    
                

                
                    
            
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

            frm5=Frame(mwindow,height=50,width=900,bg="#990066")
            frm5.grid(row=1,column=1,sticky=S+N+E+W)

            frm6=Frame(mwindow,height=580,width=900,bg="#990066")
            frm6.grid(row=2,column=1,pady=10,sticky= W+N+E+S)

            frm1=Frame(frm6,height=580,width=430,bg="#990066")
            frm1.grid(row=1,column=1,padx=10,sticky= W+N+S+E)

            frm2=Frame(frm6,height=580,width=660,bg="#990066")
            frm2.grid(row=1,column=2,padx=10,sticky= W+N+S+E)

            now=datetime.datetime.now()
            cur_date=str(str(now.day)+"-"+str(now.month)+"-"+str(now.year))
            mydate=date.today()
            cur_day=calendar.day_name[mydate.weekday()]

            date_lbl=Label(frm5,text="DATE : "+str(cur_date),fg="gray",bg="#990066")
            date_lbl.grid(row=1,column=1,sticky=W,padx=40,pady=5)

            day_lbl=Label(frm5,text="DAY : "+str(cur_day),fg="gray",bg="#990066")
            day_lbl.grid(row=1,column=2,sticky=W,padx=40,pady=5)

            c_lbl=Label(frm5,text="COURSE: "+str(course),fg="gray",bg="#990066")
            c_lbl.grid(row=1,column=3,sticky=W,padx=40,pady=5)

            s_lbl=Label(frm5,text="SEMESTER : "+str(stream),fg="gray",bg="#990066")
            s_lbl.grid(row=1,column=4,sticky=W,padx=40,pady=5)

            b_lbl=Label(frm5,text="BRANCH: "+str(sem),fg="gray",bg="#990066")
            b_lbl.grid(row=1,column=5,sticky=W,padx=40,pady=5)

            ## Tags of Frame 1

            b_lbl1=Label(frm1,text="College Id ",fg="gray",bg="#990066")
            b_lbl1.grid(row=1,column=1,sticky=W,padx=50,pady=5)

            b_lbl2=Label(frm1,text="Name",fg="gray",bg="#990066")
            b_lbl2.grid(row=1,column=2,sticky=W,padx=50,pady=5)

            ## Tags of Frame 2

            b_lbl11=Label(frm2,text="College Id ",fg="gray",bg="#990066")
            b_lbl11.grid(row=1,column=1,sticky=W,padx=30,pady=5)

            b_lbl21=Label(frm2,text="Name",fg="gray",bg="#990066")
            b_lbl21.grid(row=1,column=2,sticky=W,padx=30,pady=5)

            b_lbl22=Label(frm2,text="Mark",fg="gray",bg="#990066")
            b_lbl22.grid(row=1,column=3,sticky=W,padx=30,pady=5)
            i=0
            while(i<len(name_att)):
                out1=Label(frm1,text=str(roll_att[i]),fg="gray",bg="#990066")
                out1.grid(row=i+2,column=1,sticky=W,padx=50,pady=5)

                out2=Label(frm1,text=str(name_att[i]),fg="gray",bg="#990066")
                out2.grid(row=i+2,column=2,sticky=W,padx=50,pady=5)
                i=i+1

            global n
            n=0
            j=0
            x=0
            while(j<len(name_att1)):
                out1=Label(frm2,text=str(roll_att1[j]),fg="gray",bg="#990066")
                out1.grid(row=j+2,column=1,sticky=W,padx=30,pady=5)

                out2=Label(frm2,text=str(name_att1[j]),fg="gray",bg="#990066")
                out2.grid(row=j+2,column=2,sticky=W,padx=30,pady=5)
                invoke(j,roll_att1[j])
                j=j+1
                n=j
                x=x+10
            

            submit=Button(frm2,width=10,text="Send",bg="gray",fg="#990066",command=save)
            submit.grid(row=n+2,column=3,pady=10,sticky=S)

            mwindow.mainloop()
        

