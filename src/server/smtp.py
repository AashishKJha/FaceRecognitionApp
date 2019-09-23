import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("aashishjha.1994@gmail.com", "aashishgolu")
 
msg = "Hello!"
server.sendmail("aashishjha.1994@gmail.com", "adityanew2014@gmail.com", msg)
server.quit()
