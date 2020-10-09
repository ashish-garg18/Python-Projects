import smtplib

to = input("Enter the email of recipient\n")
content = input("Enter the content for email\n")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587) # Port for google smtp server
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com', '1234') # Enter your own email and password 
    server.sendmail('senderemail@gmail.com', to, content) 
    server.close()

sendEmail(to, content)