import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

from Locators import message

service_obj = Service(r"C:\Users\USER\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)  # maximum global timeout on you work flow used inplace of sleep time

driver.get("https://rahulshettyacademy.com/loginpagePractise")
driver.find_element(By.CLASS_NAME, "blinkingText").click()

import re
my_text = "Please email us at mentor@rahulshettyacademy.com with below template to receive response"
my_email = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", my_text)
print(my_email)

windowsopened = driver.window_handles    # It will list the windows opened according to how hey were opened
driver.switch_to.window(windowsopened[1])
time.sleep(2)
driver.close()
driver.switch_to.window(windowsopened[0])  # switching back to the parent window

driver.find_element(By.ID, "username").send_keys(my_email)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("learning")
driver.find_element(By.ID, "signInBtn").click()

print("incorrect username/password.")



