from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("zee@software.com")
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@1234")
driver.find_element(By.CLASS_NAME, "forget-password-link").send_keys("Hello@1234")
