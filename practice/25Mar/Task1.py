from time import sleep
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.ID, 'user-name').send_keys("standard_user")
driver.find_element(By.ID, 'password').send_keys("wrong")
driver.find_element(By.ID, 'login-button').click()

expected = 'https://www.saucedemo.com/inventory.html'
actual = driver.current_url

# try:
#     assert expected == actual, 'URL did not match'
# except AssertionError:
#     driver.save_screenshot('screenshot1.png')

if expected != actual:
    driver.save_screenshot('screenshot1.png')