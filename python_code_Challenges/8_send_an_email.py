import smtplib, ssl

port=465
smtp_server = "smtp.gmail.com"

sender_email = input('Enter your email address:')
reciever_email = input('Enter the recievers email address:')

password = input('Enter your password:')

message = """
This email was send using python!!
"""
#context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port) as server:
    server.login(sender_email, password)
    server.sendmail(send_mail, reciever_mail, message)


