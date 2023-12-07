
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://www.apple.com")
link = driver.current_url
baslik = driver.title
print("sayfa baslik: "+baslik)
if "apple.com" in link:
    print("Dogru, Apple sayfasindayiz: "+link)
    
driver.maximize_window()
    
driver.get("http://www.etsy.com")
link = driver.current_url
baslik = driver.title
print("sayfa baslik: "+baslik)
if "etsy.com" in link:    
    print("Etsy sayfasindayiz: "+link)
else:    
    driver.save_screenshot("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/Apple.png")    
driver.back()
baslik = driver.title
if "Apple" in baslik:
    print("Tebrikler, Apple sayfasina dondun")
else: 
    driver.save_screenshot("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/Etsy.png")
    
#şuanki pencereyi kapatır    driver.close()
driver.quit()
#driver.quit seleniumun kullandığı tüm pencereleri kapatır.


