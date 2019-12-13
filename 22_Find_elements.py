'''
1. Using find_elements we can select all check boxes at a time.

'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toolsqa.com/automation-practice-form/')
time.sleep(5)

driver.execute_script("window.scrollTo(0, 1200)")
time.sleep(5)

# To selct all check boxes
cboxes = driver.find_elements_by_xpath('//input[contains(@id,"tool-")]')

print('\n cboxes ', cboxes)

for c in cboxes:
    time.sleep(2)
    c.click()

time.sleep(10)
driver.close()