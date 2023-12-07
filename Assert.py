
from selenium import webdriver
from selenium.webdriver import Keys    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 

def Login(username, password):  
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = driver.find_element(By.ID, "flash").text
    return message

message = Login("usr","psw")
assert "Your username is invalid!" in message
time.sleep(2)
message = Login("tomsmith", "psw")    
assert "Your password is invalid!" in message  
time.sleep(2)
message = Login("tomsmith", "SuperSecretPassword!")     
assert "You logged into a secure area!" in message        
time.sleep(2)    
link = driver.current_url
assert "secure" in link
time.sleep(2)       