#Handling Java / JavaScript Alert popups using Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
name = "zoe"
service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
#alert.dismiss()

