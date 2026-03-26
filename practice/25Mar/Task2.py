from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

driver.get('https://in.pinterest.com/')
driver.maximize_window()
actions = ActionChains(driver)

folder = os.path.join(os.getcwd(), 'ss')
os.makedirs(folder, exist_ok=True)
driver.save_screenshot(f'{folder}/screenshot.png')

sleep(2)
ele = driver.find_element(By.XPATH, '(//div[@class="ADXRXN gEQpi5"])[19]')
actions.scroll_to_element(ele).perform()
ele.screenshot(f'{folder}/screenshot_element.png')