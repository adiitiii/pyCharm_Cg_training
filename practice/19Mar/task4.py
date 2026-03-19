from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
driver.implicitly_wait(10)
sleep(5)
driver.find_element(By.ID, 'multipleFilesInput').send_keys(r"C:\Users\adima\OneDrive\Desktop\renu mummy.jpeg" + "\n" +
r"C:\Users\adima\OneDrive\Desktop\NehalMaheshwari_PanCard.jpeg")