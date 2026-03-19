from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
ele = driver.find_elements(By.XPATH, "//a[@class='nav-a  ']")
for e in ele:
    print(e.get_attribute('href'))
print(len(ele))