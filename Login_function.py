
from selenium import webdriver
from selenium.webdriver import Keys    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window() 
"""driver.get("https://the-internet.herokuapp.com/login")
#wrong username test
Login_username = driver.find_element(By.ID, "username").send_keys("wrongusername")
time.sleep(2)
Login_password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(2)
Login_Login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(2)
message1 = driver.find_element(By.ID, "flash").text

if "Your username is invalid!" in message1:
    print("wrong username is working correctly")
else:
    print("error:wrong username is not working")   
    save_screenshot()

#wrong password test
driver.get("https://the-internet.herokuapp.com/login")
Login_username = driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(2)
Login_password = driver.find_element(By.ID, "password").send_keys("WrongPassword")
time.sleep(2)
Login_Login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(2)
message2 = driver.find_element(By.ID, "flash").text

if "Your password is invalid!" in message2:
    print("wrong password is working correctly")
else:
    print("error:wrong password is not working")    
    save_screenshot()

#correct logging test
driver.get("https://the-internet.herokuapp.com/login")
Login_username = driver.find_element(By.ID, "username").send_keys("tomsmith")
time.sleep(2)
Login_password = driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
time.sleep(2)
Login_Login = driver.find_element(By.CSS_SELECTOR, "button.radius").click()
time.sleep(2)
message3 = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message3:
    print("Logging operation test works well!")
else:
    print("error: logging has mistaken!")  
    save_screenshot()    
time.sleep(3)    

#title check after logged in
correct_message = driver.find_element(By.CSS_SELECTOR, "h2").text
if "Secure Area" in correct_message:
    print("Well, page title is as usual!")
else:
    print("error: something wrong in the page title!")    

#logout button clicked
driver.find_element(By.XPATH, "//div[@id='content']//a[@href='/logout']").click()

if "login" in driver.current_url:
    print("OK: got back to the login page")
else: 
    print("error: it couldn't be gotten back to the login page")
    save_screenshot()
    
time.sleep(5)    
"""


    
def Login(username, password):  
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    message = driver.find_element(By.ID, "flash").text
    return message

message = Login("usr","psw")

if "Your username is invalid!" in message:
    print("wrong username is working correctly")
else:
    print("error:wrong username is not working")   
   
time.sleep(2)
    
message = Login("tomsmith", "psw")    

if "Your password is invalid!" in message:
    print("wrong password is working correctly")
else:
    print("error:wrong password is not working")    

time.sleep(2)
   
message = Login("tomsmith", "SuperSecretPassword!")     

if "You logged into a secure area!" in message:
    print("Logging operation test works well!")
else:
    print("error: logging has mistaken!")  
       
time.sleep(2)    

link = driver.current_url
if "secure" in link:
    print("link includes secure.")
else:
    print("error:link does not includes secure!")    

time.sleep(2)       