from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://www.python.org')
d.maximize_window()
time.sleep(5)

# Take screenshot
d.save_screenshot(r'C:\Users\smellamp\Desktop\ROBOT\SRIRAM.png')
d.close()