from selenium import webdriver
import time 


driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/login?lang=en")

w_title = driver.title

print("\n title is :", w_title)

# verify the title is expected or not :

# if w_title != 'Login on Twitter1': raise AssertionError("Title is not expected")

assert w_title == 'Login on twitter', "Title is not excepted1"

