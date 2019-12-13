from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")
time.sleep(5)
driver.refresh()
time.sleep(7)
driver.refresh()
time.sleep(5)
driver.close()


