from selenium import webdriver
# chrome driver
from selenium.webdriver.chrome.service import Service
# How to run tests in Chrome, Firefox, Edge Browser
# How to invoke Chrome browser and load the Website to automate
#  Basic WebDriver methods to get Title, url and close the session

# ------------chrome browser
service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)  # driver has full control over/invoke chrome

# ------------firefox browser
#service_obj = Service(r"C:\Users\USER\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")
#driver = webdriver.Firefox(service=service_obj)

# ------------edge browser

#service_obj = Service(r"C:\Users\USER\Downloads\edgedriver_win64\msedgedriver.exe")
#driver = webdriver.Edge(service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#driver.minimize_window()
driver.back()
driver.refresh()
driver.forward()
driver.close()  # closes the browser


