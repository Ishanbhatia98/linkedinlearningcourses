from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

#url = '/Users/ishan/desktop/llc/python_automation_and_testing/ch3/html_code.html'
url = 'file:///Users/ishan/Desktop/LLC/python_automation_and_testing/ch3/html_code.html'

driver.get(url)

select = Select(driver.find_element_by_name('numReturnSelect'))

select.select_by_index(4)
time.sleep(2)

select.select_by_visible_text("500")
time.sleep(2)

select.select_by_value("250")
time.sleep(2)

options = select.options
print(*options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)

driver.close()
