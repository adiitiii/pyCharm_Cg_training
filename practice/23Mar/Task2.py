'''
TASK2

https://www.nike.in/
perform mouse hover action on kids in nav bar and after sleep of sometime give click action then give a scroll and then perfrom click action on "Shop" and
after that scroll and click on some other element and then select size and click add to bag
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

driver.get('https://www.nike.com/')
driver.maximize_window()
actions = ActionChains(driver)
sleep(2)
kids = driver.find_element(By.XPATH, '//span[text()="Kids"]')
actions.move_to_element(kids).perform()
sleep(3)
actions.click(kids).perform()

driver.switch_to.window(driver.window_handles[1])
sleep(2)
shop = driver.find_element(By.XPATH, '//a[text()="Shop"]')
actions.scroll_to_element(shop).perform()
sleep(2)
actions.click(shop).perform()

shoe = driver.find_element(By.XPATH, '//a[@aria-labelledby="aria-label-24788611-1 aria-label-24788611-2"]')
actions.click(shoe).perform()
sleep(2)

driver.switch_to.window(driver.window_handles[2])
size = driver.find_element(By.XPATH, '//label[text()="UK 1.5"]')
actions.click(size).perform()
sleep(2)
cart = driver.find_element(By. XPATH, '//button[text()="Add to Bag"]')
actions.click(cart).perform()

driver.quit()