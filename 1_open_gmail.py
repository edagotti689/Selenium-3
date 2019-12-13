from selenium import webdriver
import time

# Open a Browser 
driver = webdriver.Chrome()

# To Maximize window
driver.maximize_window()
time.sleep(3)

# Open a URL
driver.get('https://accounts.google.com/')
time.sleep(3)

# To enter username in text box based on ID identifier
uo = driver.find_element_by_id('identifierId')
uo.send_keys('sriram.python111')
time.sleep(5)

# Click on next button after entering gmail based on xpath identifier
un = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
un.click()
time.sleep(3)

# Enter Password based on name
driver.find_element_by_name('password').send_keys('password')
time.sleep(3)

# Click Next button using xpath element after entered password
driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()


time.sleep(10)

# Close a browser
driver.close()

