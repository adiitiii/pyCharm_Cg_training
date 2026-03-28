from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(2)
ele = driver.find_element(By.XPATH, '//a[text()="Facebook"]')

actions = ActionChains(driver)
actions.scroll_to_element(ele)
ele.click()

sleep(2)
driver.switch_to.window(driver.window_handles[1])
sleep(2)
print(driver.current_url)
# sleep(3)
# driver.switch_to.alert
# driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('hjv')
driver.find_element(By.XPATH, '(//input[@name="email"])[2]').send_keys('hello')
driver.find_element(By.XPATH, '(//input[@name="pass"])[2]').send_keys("kreeeee234")
driver.find_element(By.XPATH, '(//span[text()="Log in"])[3]').click()