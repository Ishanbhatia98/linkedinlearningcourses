#not working as expected


from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()


url = 'http://jqueryui.com/droppable'
driver.get(url)

driver.switch_to_frame(0)

action_chains = ActionChains(driver)

source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')


action_chains.drag_and_drop_by_offest(source, 100, 100).perform()
time.sleep(2)

action_chains.drag_and_drop(source, target).perform()
time.sleep(2)

driver.close()
