from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)

# Move the window to position x/y
driver.set_window_position(100, 100)
time.sleep(5)

print(driver.get_window_position())
driver.close()
