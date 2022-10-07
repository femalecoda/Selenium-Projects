# Check buttons and Radio buttons.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(r"C:\Users\USER\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# for button that have variable location use the condition method
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']") # click option button 2

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("id") == "checkBoxOption2":
        checkbox.click()
        assert checkbox.is_selected()
        break

#for buttons with specific location use their index
radiobutton = driver.find_elements(By.CSS_SELECTOR, ".radioButton")  # click radio button2
radiobutton[2].click()
assert radiobutton[2].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

#radiobutton = driver.find_elements(By.XPATH, "//input[@type='radio']") # click radio button2
#print(len(radiobutton))
#for radio in radiobutton:
#    if radio.get_attribute("value") == "radio2":
#        radio.click()
#        break




