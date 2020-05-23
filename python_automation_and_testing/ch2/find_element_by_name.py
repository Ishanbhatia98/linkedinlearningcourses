from selenium import webdriver

url = "file:///Users/ishan/Desktop/LLC/python_automation_and_testing/ch2/html_code.html"

driver = webdriver.Chrome()

driver.get(url)

username = driver.find_element_by_name("username")

print("My input element is", username)

driver.close()
