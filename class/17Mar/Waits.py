from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
# var = o.headless
driver = Chrome(options=o)

driver.implicitly_wait(5)

driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
driver.maximize_window()

driver.find_element(By.XPATH, "//button[text()='Start']").click()
name = driver.find_element(By.XPATH, '//div[@id="finish"]').text
print(name)
