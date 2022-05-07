#Chris - Rick Roll
import webbrowser
import time
import smtplib, ssl

count = 0
timer = 0 
while timer <3:
    time.sleep(1)
    webbrowser.open("https://www.youtube.com/watch?v=O91DT1pR1ew")
    count = count + 1

def sendemail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "insert sending email here"
    password = "insert sending email's password here"
    receiver_email = "insert target email here"

    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context = context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print(e)
    finally:
        server.quit("https://www.youtube.com/watch?v=O91DT1pR1ew")