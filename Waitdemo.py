# implicit wait
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "zoe"
service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)  # maximum global timeout on you work flow used inplace of sleep time

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()  # this is the chain method (chain parent to child)

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

