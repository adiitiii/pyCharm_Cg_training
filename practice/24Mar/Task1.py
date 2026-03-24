from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''
While working with iframes it gives NoSuchElementException because 1. locator is correct or not 2. if page is loading slower n selenium is wokring fast
3. means its i frame diver control is in main frame only

to switch b/w frames
1. index
2. name
3. web element (locator)

driver.switch_to.frame(0)
'''
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://x.com/")
driver.maximize_window()

sleep(2)
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]'))
switch = driver.find_element(By.XPATH, '//span[. ="Sign up with Google"]')
switch.click()
