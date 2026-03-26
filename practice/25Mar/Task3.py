from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://www.lenskart.com/')
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//a[@aria-label="EYEGLASSES"]').click()
expected = driver.current_url
actual = 'https://www.lenskart.com/eyeglasses.html'

assert expected == actual, 'URL mismatch'

driver.find_element(By.XPATH, '//select[@id="sortByDropdown"]').click()
sleep(2)
driver.find_element(By.XPATH, '//option[text()="Most Viewed"]').click()
sleep(2)
driver.save_screenshot('lenses.png')
