from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shoes')
sleep(2)
driver.find_element(By.XPATH, '//div[@aria-rowindex="4"]').click()
sleep(3)
driver.find_element(By.XPATH, '//span[@class="a-dropdown-label"]').click()
driver.find_element(By.ID, 's-result-sort-select_4').click()
sleep(3)
driver.find_element(By.XPATH, '(//i[@class="a-icon a-icon-checkbox"])[1]').click()
sleep(3)
driver.find_element(By.XPATH, '//img[@src="https://m.media-amazon.com/images/I/311lw6BsAUL._AC_UL320_.jpg"]').click()
sleep(3)
name = driver.find_element(By.XPATH, '(//span[contains(text(),"        Buckaroo Vegan")])[1]').text
price = driver.find_element(By.XPATH, '(//span[text()="2,315"])[1]').text
print(f'Name is {name} and price is {price}')


