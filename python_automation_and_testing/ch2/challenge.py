#not working as expected

from selenium import webdriver

import time

driver = webdriver.Chrome()

url = "http://www.seleniumhq.org/"
url_ = "https://selenium-python.readthedocs.io/"

driver.get(url)

q_element = driver.find_element_by_id('gsc_i_id1')
print("The q element object: ", q_element)

q_name_element = driver.find_element_by_name('q')
print("The element by object with name 'q': ", q_name_element)

getting_started_xpath = driver.find_element_by_xpath('///h2')
print("The getting Started element is: ", getting_started_xpath)

selenium_sponsors_class = driver.find_element_by_class_name('selenium-sponsors')
print("The element with class name 'selenium-sponsors': ", selenium_sponsors_class)

time.sleep(25)
driver.close()
