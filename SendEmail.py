import smtplib, ssl



port = 587
smtp_server = "smtp.gmail.com"
sender_email = "SeuEmail@gmail.com"
receiver_email = "Destinario@gmail.com"
password = input("Coloque sua senha:")
message = """\
Subject: Chegou Python Bi-Bi!

Esta Mensagem Foi Enviada usando Python."""


#subject manda o assunto e logo em baixo a mensagem que deseja mandar

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)