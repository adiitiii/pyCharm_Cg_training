from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(5)
driver.get('https://www.decathlon.in/')

driver.maximize_window()
driver.find_element(By.XPATH, "//a[contains(@href,'/Winter-Collection')]").click()
driver.find_element(By.XPATH, "//a[contains(@href,'contents.mediadecathlon')]").click()