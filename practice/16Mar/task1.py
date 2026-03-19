from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.flipkart.com/')
sleep(3)
driver.find_element(By.ID, "_58bkzq6r _3n8fna1co _3n8fna10j _3n8fnaod _3n8fna1 _3n8fnac7 _58bkzq4 _1i2djtb9 _1i2djt0").send_keys('jeans for women')
sleep(3)