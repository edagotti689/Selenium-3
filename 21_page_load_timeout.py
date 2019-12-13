from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(30)
# Open a URL
driver.get('https://www.toolsqa.com/automation-practice-form/')
time.sleep(5)