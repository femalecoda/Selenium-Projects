from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

service_obj = Service(r"C:\Users\USER\Downloads\geckodriver-v0.31.0-win64\geckodriver.exe")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsopened = driver.window_handles    # It will list the windows opened according to how hey were opened

driver.switch_to.window(windowsopened[1])
print(driver.find_element(By.XPATH, "//h3").text)
driver.close()
driver.switch_to.window(windowsopened[0])  # switching back to the parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text
