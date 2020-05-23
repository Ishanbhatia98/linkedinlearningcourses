from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///Users/ishan/Desktop/LLC/python_automation_and_testing/ch2/html_code.html")

content = driver.find_element_by_class_name("content")

print("My class element is: ", content)

driver.close()
