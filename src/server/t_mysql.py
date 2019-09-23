import mysql.connector
list_detect=['13CS03','13CS07'

cnx = mysql.connector.connect(user='root', password='adi', host='127.0.0.1', database='project')
if(cnx):
    if(cnx):
        cursor=cnx.cursor()
        q1="select count(*) from sregister"
        cursor.execute(q1)
        result1=cursor.fetchone()
        t_row=result1[0]
        
        while(i<t_row):
            q="insert into attendance_m (mark) values (1) where cid=%s"
            data1=(list_detect[i],)
            print(data1)
            cursor.execute(q,data1)
            i=i+1
    
