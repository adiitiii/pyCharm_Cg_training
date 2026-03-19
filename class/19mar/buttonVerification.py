from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# sleep(2)
# ele = driver.find_element(By.XPATH, "//div[@aria-label='Log in']")
# print(ele.is_displayed())
# print(ele.is_enabled())

# driver.get("https://www.naukri.com/mnjuser/homepage")
# driver.maximize_window()
# driver.implicitly_wait(10)
# sleep(3)
# ele = driver.find_element(By.CLASS_NAME, "g-recaptcha")
# print(ele.is_displayed())
# print(ele.is_enabled())

driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()
driver.implicitly_wait(10)
sleep(3)
check = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[1]')
print(check.is_selected())
check2 = driver.find_element(By.XPATH, '(//input[@type="checkbox"])[2]')
print(check2.is_selected())
# check.click()