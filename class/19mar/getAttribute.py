from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_element(By.XPATH,'//a[@class="gb_A"]')
print(ele.get_attribute('aria-label'))
