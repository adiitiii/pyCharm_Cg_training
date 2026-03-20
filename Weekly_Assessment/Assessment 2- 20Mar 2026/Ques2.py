from time import sleep

from selenium.webdriver.support import expected_conditions as EC #EC is alias name
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.saucedemo.com/')
driver.maximize_window()
wait = WebDriverWait(driver, 20)

#Clicking on the username input field using ID selector
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).click()

#sending "standard_user" as input using ID selector
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")

#clicking the password input field for entering the password using ID selector
wait.until(EC.presence_of_element_located((By.ID, "password"))).click()

#sending "secret_sauce" as input in password field by using ID selector
wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("secret_sauce")

#clicking the login button
wait.until(EC.presence_of_element_located((By.ID, "login-button"))).click()

#fetched the title using explicit wait using XPATH
title = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Products']"))).text
print(title)

#printing all the products name using XPATH
prod_name = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_name "] ')))
for p in prod_name:
    print(p.text)

#printing all the products name using XPATH
prod_price = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="inventory_item_price"] ')))
for p2 in prod_price:
    print(p2.text)

#added the fourth item in cart
wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))).click()