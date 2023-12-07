
from selenium import webdriver
from selenium.webdriver import Keys    
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:/Users/utkut/OneDrive/Masaüstü/Python_Selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
haftanin_seckin_maddesi = driver.find_element(By.ID, "mp-tfa")
seckin_madde_yazisi = haftanin_seckin_maddesi.text
seckin_madde_yazisi = seckin_madde_yazisi.split(",")[0]
print(seckin_madde_yazisi)
time.sleep(2)
biliyor_muydunuz = driver.find_element(By.ID, "mp-bm").text
biliyor_muydunuz = biliyor_muydunuz.split(".")[0:1]

print("biliyor muydunuz?:".join(biliyor_muydunuz))


driver.quit()



"""aramakutusu = driver.find_element(By.CSS_SELECTOR, "input#searchbox_input")"""

