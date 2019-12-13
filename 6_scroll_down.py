from selenium import webdriver
import time

# Open a Chrome Browser
d = webdriver.Chrome();
d.maximize_window()
d.get("https://www.citibank.co.in/ibank/login/IQPin1.jsp?dOfferCode=LOANONCRED")
time.sleep(6)

# To Scroll down page
d.execute_script("window.scrollTo(0, 300)")
time.sleep(6)
# To Scroll up page
d.execute_script("window.scrollTo(500, 0)")
time.sleep(10)
d.close()




