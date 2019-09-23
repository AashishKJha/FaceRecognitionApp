import mysql.connector 
cnx = mysql.connector.connect(user='root', password='aashishgolu', host='127.0.0.1', database='project') 
cursor=cnx.cursor()
q= "INSERT INTO sreg  (fneme , fname) VALUES(%s,%s)"
d=('aashish kumar Jha','aashish')
t=cursor.execute(q,d)
if(t):
    print("ok")
else:
    print("not ok")
    
cnx.commit()
cursor.close()
cnx.close() 
