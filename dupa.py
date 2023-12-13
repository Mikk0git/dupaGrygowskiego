import pyautogui
import time
import os 


print("---")
os.mkdir("tmp")

i = 1
while i < 10:
    screenshot = pyautogui.screenshot()
    screenshot.save(f"tmp/{i}.png")
    print(f"screen captured {i}")
    i=i+1
    time.sleep(2)

