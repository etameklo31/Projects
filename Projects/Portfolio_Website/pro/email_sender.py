from email.message import EmailMessage
import ssl
import smtplib

email_sender = '' # this is where you put email
email_password = '' # this is where your email password which you get from the 2 factor authentication in google

email_reciever = '' # this is where you put the email recipient 

subject = "Don't forget to subscribe"
body = "Hi, nice to meet!"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
