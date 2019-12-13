from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.python.org")

## click on specified element
time.sleep(5)
driver.find_element_by_xpath('//*[@id="downloads"]/a').click()
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()


