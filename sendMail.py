import smtplib
import weatherapp
import token_key

message = weatherapp.message

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(token_key.sender_mail, token_key.mail_pswd)
server.sendmail(token_key.sender_mail, token_key.reciver_mail, message)
server.quit()
