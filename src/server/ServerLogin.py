import socket
address = ("192.168.43.67", 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(10000)
flag=0
class StartServer:
    def __init__(self):
        
    
    
        print("Server Running...")

        global course
        global sem
        global stream

        while True:
            try:
                
                client, address = s.accept()
                print("Client arrived " , address)

                client_data = client.recv(2048)
        ##        print("a")
                client_data_s = client_data.decode("utf-8")
                print(client_data_s)
        ##        print("b")
                client_data=client_data_s.split("/")
        ##        print("c")
                print(client_data)

                if(str(client_data[0])=="Login"):
                    import mysql.connector
                    cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
                    if(cnx):
                        cursor=cnx.cursor()
                        try:
                            q=("select password from t_register where email=%s")
                            data=(client_data[1],)
                            cursor.execute(q,data)
                            result=cursor.fetchone()
                            print(result[0])
                            print(client_data[1])
                            if(result[0]==client_data[2]):
                                server_data='1'
                                server_data = server_data.encode("utf-8")
                                client.send(server_data)
                            else:
                                server_data='0'
                                server_data=server_data.encode("utf-8")
                                client.send(server_data)
                        except Exception as e:
                            print( type(e))
                    cnx.commit()
                elif(str(client_data[0])=="LoginSuccessful"):
                    server_data='1'
                    server_data = server_data.encode("utf-8")
                    client.send(server_data)
                    course=client_data[1]
                    sem=client_data[2]
                    stream=client_data[3]

                elif(client_data[0]=="Department"):

                    server_data='1'
        ##            print(server_data)
                    server_data = server_data.encode("utf-8")
                    client.send(server_data)

                    course=client_data[1]
                    sem=client_data[2]
                    stream=client_data[3]
                    
                elif(str(client_data[0])=="Image"):
                    server_data='1'
                    server_data = server_data.encode("utf-8")
                    client.send(server_data)
                    
        ##            print("aashish")
                    
                    filename = open('input.jpg', 'wb')
                    while True:
                        strng = client.recv(512)
                        if not strng:
                            flag=1
                            break
                        filename.write(strng)
        ##            print("out of loop")
                    filename.close()
                    if(course!="" and sem!="" and stream!=""):
                        from traineer import Trainee
                        Trainee(course,sem,stream)
                        from detector import detect
                        tup=detect(course,sem,stream,client).detection()
                        from datalist import database
                        global tup1
                        tup1=database(tup[0],tup[1],tup[2]).WOL()
                elif(str(client_data[0])=="Profile"):
                    import mysql.connector
                    cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
                    if(cnx):
                        cursor=cnx.cursor()
                        try:
                            q=("select * from sregister where cid=%s")
                            p=str(client_data[1])
                            data=(p,)
                            cursor.execute(q,data)
                            result=cursor.fetchone()
                            name=str(result[1])+" "+str(result[2])+" "+str(result[3])
                            s_data=name+"/"+str(result[4])+"/"\
                                    +str(result[5])+"/"+str(result[6])+"/"+str(result[7])+"/"+str(result[8])+"/"\
                                    +str(result[9])+"/"+str(result[10])+"/"+str(result[11])+"/"+str(result[12])+"/"\
                                    +str(result[16])+"/"+str(result[17])
                            if(str(s_data)!=""):
                                s_data = s_data.encode("utf-8")
                                client.send(s_data)
                                path="Photo/FullImage/"+str(result[11])+"/"+str(result[16])+"/"+str(result[12])+"/"+p[0]+p[1]+p[4]+p[5]+".jpg"
                                print(path)
                                f=open(str(path),'rb')
                                d=f.read(512)
                                while True:
                                    if not d:
                                        print("empty")
                                        break
                                    client.send(d)
                                    print("ok")
                                    d=f.read(512)
                                    
                                    
                                f.close()
                                client.close()
                                print("File Close")
                                
                            else:
                                server_data='0'
                                server_data=server_data.encode("utf-8")
                                client.send(server_data)
                        except Exception as e:
                            print( str(type(e))+ str(e))
                    cnx.commit()
                    
                        
                elif(str(client_data[0])=="Request"):
                    print("request")
                    print(tup1)
                    server_data = '1'
                    server_data = server_data.encode("utf-8")
                    client.send(server_data)
                    
                    server_data = str(tup1).encode("utf-8")
                    client.send(server_data)
                    client.close()
                elif(str(client_data[0])=="Status"):
                    emp=""
                    att=""
                    i=0
                    import mysql.connector
                    cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
                    if(cnx):
                        cursor=cnx.cursor()
                        try:
                            q=("select distinct fname,mname,sname,eid,cid,email from sregister where course=%s AND sem=%s AND stream=%s ")
                            data=(str(client_data[1]),str(client_data[2]),str(client_data[3]))
                            
                            cursor.execute(q,data)
                            result=cursor.fetchall()
                            cnx.commit()
                            print(result)
                            while(i<len(result)):
                                x=str(result[i][0])+" "+str(result[i][1])+" "+str(result[i][2])+"/"+str(result[i][3])+"/"+str(result[i][4])+"/"+str(result[i][5])
                                emp=emp+x+"//"
                                i=i+1
                            i=0
                            while(i<len(result)):
                                q1=("select count(mark) from attendance_m where cid=%s AND mark=%s")
                                data1=(str(result[i][4]),int(1))
                                cursor.execute(q1,data1)
                                att=att+str(cursor.fetchone()[0])+"/"
                                cnx.commit()
                                i=i+1
                            cursor.close()
                            cnx.close()
                            fin=emp+"@@"+att
                            fin=fin.encode("utf-8")
                            client.send(fin)
                            client.close()
                            
                            
                        except Exception as e:
                            print(str(type(e))+str(e))
                    
                    

                elif(str(client_data[0]) == "End"):
                    server_data = '1'
                    server_data = server_data.encode("utf-8")
                    client.send(server_data)

                    strng = client.recv(1024)

                    if(strng != ""):
                        from final import Final_att
                        Final_att(strng)
                    
                    print(strng)
                    
        ##            s.close()
                    print('End')
                else:
                    print("Error")
            except Exception as e:
                print( type(e), " - ", str(e) )



    
