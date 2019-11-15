import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("", "")
# Add multiple emails to send mail
msg = "Hello!"
server.sendmail("", "", msg)
server.quit()
