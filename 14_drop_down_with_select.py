from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get('https://www.toolsqa.com/automation-practice-form/')
time.sleep(5)

continents = Select(driver.find_element_by_id('continents'))

# To select a value based on text
continents.select_by_visible_text('Europe')
time.sleep(10)

# To select a value based on value
#continents.select_by_value('Europe')

# To select a value based on index
continents.select_by_index(3)

#time.sleep(100)
#driver.close()
'''
1.UnexpectedTagNameException::

selenium.common.exceptions.UnexpectedTagNameException: Message: Select only work
s on <select> elements, not on <div>
'''





