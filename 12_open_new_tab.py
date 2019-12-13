from selenium import webdriver
import time

d = webdriver.Chrome()
d.maximize_window()

d.get("https://accounts.google.com/")
time.sleep(5)

## Open a new tab with URL
d.execute_script("window.open('http://bings.com')")
time.sleep(5)


## Open a new tab without URL
d.execute_script("window.open()")

## Open a new URL on same tab
d.execute_script('window.open("https://www.pylint.org/","_current")')
time.sleep(5)

# TO close only current tab
#d.close()

# TO close all tabs 
# d.quit()







