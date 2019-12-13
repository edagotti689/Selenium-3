from selenium import webdriver
import time

# Open Chrome Browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org")

## Get text based on xpath
value = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

print('\n Text is :', value)
time.sleep(4)

# Verify text is expected or not 
#if value != 'Downloads1': raise AssertionError('Text is not expected')

assert value == 'Downloads1',  'Text is not expected'

time.sleep(4)
driver.close()


