from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'emanueltameklo31@gmail.com'
email_password = 'abdc eoom hyhd folg'

email_reciever = 'berry.belcher23@gmail.com'

subject = "Don't forget to subscribe"
body = "You are a penis pirate :)"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
