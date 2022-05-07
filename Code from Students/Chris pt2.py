#Chris - Email Spam
import smtplib, ssl

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
        server.quit()
        print("email sent")

sendemail("beans")
