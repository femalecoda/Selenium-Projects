from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
# Using XPATH
#driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("zee@software.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@1234")
#driver.find_element(By.ID, "confirmPassword").send_keys("Hello@1234")
#driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Using CSS-Selector
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(1) input").send_keys("zee@software.com")
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello12345")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello12345")
driver.find_element(By.XPATH, "//button[text() ='Save New Password']").click()

