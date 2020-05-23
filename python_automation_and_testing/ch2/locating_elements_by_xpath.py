from selenium import webdriver

driver = webdriver.Chrome()

driver.get("file:///Users/ishan/Desktop/LLC/python_automation_and_testing/ch2/html_code.html")

login_form_absolute = driver.find_element_by_xpath("/html/body/form[1]")
login_form_relative = driver.find_element_by_xpath("//form[1]")
login_form_id = driver.find_element_by_xpath("//form[@id='loginForm']")

print("My xpath element is: ", login_form_relative) 

driver.close()
