from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
o.add_experimental_option("prefs", {'safebrowsing.enabled':True}) #telling it that theres an authorised person trying to download
o.add_argument("--disable-notifications") #unwanted notifications wont come
driver = Chrome(options=o)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# alert1 = driver.find_element(By.XPATH, '//button[text()="Simple Alert"]')
# alert1.click()
# sleep(2)
# alert = driver.switch_to.alert
# alert.accept()
#
# alert2 = driver.find_element(By.ID, 'confirmBtn')
# alert2.click()
# sleep(2)
# a = driver.switch_to.alert
# # a.dismiss()
# a.accept()
#
# alert3 = driver.find_element(By.ID, 'promptBtn')
# alert3.click()
# sleep(2)
# a = driver.switch_to.alert
# a.send_keys("aditi")
# sleep(2)
# a.accept()

# driver.get('https://demoqa.com/upload-download')
# driver.maximize_window()
# # driver.find_element(By.ID, 'downloadButton').click()
# # sleep(2)
# choose = driver.find_element(By.ID, 'uploadFile')
# choose.send_keys(r"C:\Users\adima\OneDrive\Desktop\NehalMaheshwari_AadharCard.pd
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT, 'Python 3.14.3').click()f")

driver.get('https://www.easemytrip.com/')
sleep(3)
