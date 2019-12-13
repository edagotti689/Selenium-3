from selenium import webdriver
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get('https://www.toolsqa.com/automation-practice-form/')
time.sleep(5)

# Select radio button
driver.find_element_by_id('sex-0').click()

time.sleep(10)
#driver.close()