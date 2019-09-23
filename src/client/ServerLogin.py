import socket
address = ("192.168.43.67", 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(10000)
flag=0

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
                    q=("select password from sregister where email=%s")
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
                        break
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
                tup=detect(stream,client).detection()
                from datalist import database
                global tup1
                tup1=database(tup[0],tup[1],tup[2]).WOL()
                
        elif(str(client_data[0])=="Request"):
            print("request")
            print(tup1)
            server_data = '1'
            server_data = server_data.encode("utf-8")
            client.send(server_data)
            
            server_data = str(tup1).encode("utf-8")
            client.send(server_data)

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



        
