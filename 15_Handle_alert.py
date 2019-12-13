from selenium import webdriver
from time import sleep

d = webdriver.Chrome()
d.maximize_window()

d.get(r'C:\INST\COURSES\3_SELENIUM/alert_2.html')
d.find_element_by_xpath('/html/body/button').click()

sleep(3)
alert = d.switch_to.alert

#  To get alert message
print(alert.text)
sleep(5)

## To accept alert
alert.accept()

# alert.accept() – used to accept the Alert
# alert.dismiss() – used to cancel the Alert
# alert.send_keys() – used to enter a value in the Alert text box.

sleep(10)
d.close()

