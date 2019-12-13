from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(5)

#Get window size
print(driver.get_window_size())
time.sleep(5)

# Resize the window to the screen width/height
driver.set_window_size(500, 400)
time.sleep(5)

print(driver.get_window_size())

# Move the window to position x/y
driver.set_window_position(200, 400)
time.sleep(5)
print(driver.get_window_size())
driver.close()
