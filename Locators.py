from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
# # some locators selenium supports: ID, Xpath, CSS-Selector, Class-Name, Name, LinkText ********************
#driver.find_element(By.NAME, "name").send_keys("Zoe", " ", "John")
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

#  using XPATH write syntax like so: eg(using xpath for submit button)
# //tagename (of the element)[@attribute (of the element)= 'value'] of the element
#//tagename[@attribute = 'value'] - By.XPATH,"//input[@type = 'submit']"

driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)

#  using CSS-Selector write syntax like so: eg(using CSS-Selection for input name)
#tagename[@attribute='value'] - By.CSS-SELECTOR, "input[@type='name']"
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Crystal", " ", "brooks")
# shortcut to CSS (#ID value), (.Class-name)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
#driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.XPATH, "//input[@type='date']").send_keys("9-1-2022")
#driver.find_element(By.XPATH, "//input[@value='option2']").click()
#driver.find_element(By.CSS_SELECTOR, "//input[@type='radio']").click()
#driver.find_element(By.CLASS_NAME, "form-control").get_property("111990")
assert "Success" in message
driver.find_element(By.XPATH, "//input[@name='name']").send_keys(" ", "Thank you")

#driver.close