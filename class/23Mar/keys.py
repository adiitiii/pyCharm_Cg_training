from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

# KEYBOARD ACTIONS
# Using Keys we can take keyboard inputs, send_keys(key.ENTER)

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.amazon.in/')

sleep(2)
ele = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(2)
ele.send_keys("dresses")
ele.send_keys(Keys.ENTER)