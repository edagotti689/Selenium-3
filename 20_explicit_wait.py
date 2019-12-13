from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://selenium-python.readthedocs.io")


# To create wait object
wait = WebDriverWait(driver, 10)

r = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/ul/li[5]/a')))
r.click()


time.sleep(10)
driver.close()

