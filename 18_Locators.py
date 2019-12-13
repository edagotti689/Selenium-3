from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()


# Open a URL
driver.get('https://www.google.com/')
time.sleep(5)

#e = driver.find_element_by_link_text('Gmail')
#e.click()
#print(e.text)

#elem = driver.find_element_by_partial_link_text("Gma")
#print(elem.text)

#el2 = driver.find_element_by_tag_name('a')
#print(el2.text)

e = driver.find_element_by_class_name('gb_e')
#e.click()
print(e.text)

time.sleep(3)
driver.close()


