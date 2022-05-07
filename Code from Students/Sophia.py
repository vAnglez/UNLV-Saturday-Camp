#Sophia Seitz - Email Spam
import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "insert sending email here"
    password = "insert sending email's password here"
    receiver_email = "insert target email here"

    context = ssl.create_default_contest ()

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    except Exception as e:
        print (e)
    finally:
        server.quit 

sendEmail (" Hello ___, I am a unicorn named Chris will youn be my friend??? I would so like to play pokemon sword and shield, and I really like drawing and i have these rare pokemon cards and i also need this mega audino card. I have a coupon right now and I was hoping you culd get these Jockey coupons that have 75% percent off any clothing if you buy 20 dollars in stuff. I just need you to sign here--- ")