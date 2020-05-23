from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///Users/ishan/Desktop/LLC/python_automation_and_testing/ch2/html_code.html")

login_form = driver.find_element_by_id('loginForm')

print("My login form element is " , login_form)

driver.close()
