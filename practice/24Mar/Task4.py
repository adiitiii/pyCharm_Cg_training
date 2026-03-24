'''
TASK4
open internet herokkuapp website click js alerts do all three alerts n print what's inside it
'''
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
actions = ActionChains(driver)

driver.get('https://the-internet.herokuapp.com/')
driver.maximize_window()
sleep(2)

alerts = driver.find_element(By.XPATH, '//a[text()="JavaScript Alerts"]')
actions.scroll_to_element(alerts).perform()
alerts.click()

sleep(2)
alert1 = driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]')
alert1.click()
a1 = driver.switch_to.alert
print(a1.text)
a1.accept()

alert2 = driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]')
alert2.click()
a2= driver.switch_to.alert
print(a2.text)
a2.accept()


alert3 = driver.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]')
alert3.click()
a3 = driver.switch_to.alert
print(a3.text)
a3.send_keys("aditi the best")
a3.accept()