from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
ACTION CHAINS
1. It will create an object
2. Store the action
3. Perform -> .perform() # action will not occur except this
n number of actions can be stored but to perform it you need to use the method
'''

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# singleClick = driver.find_element(By.XPATH, '//button[text()="Click Me"]')
# dblClick = driver.find_element(By.XPATH, '//button[text()="Double Click Me"]')
# rightClick = driver.find_element(By.XPATH, '//button[text()="Right Click Me"]')
# actions = ActionChains(driver) #for this driver (chrome browser) actions chains would be applied
# sleep(2)
# actions.click(singleClick).perform()
# sleep(2)
# actions.double_click(dblClick).perform()
# sleep(2)
# actions.context_click(rightClick).perform()
# ele = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
# sleep(2)
# ele.send_keys(Keys.ENTER)


'''
METHODS
'''
#MANUAL SCROLL: scrolltoelement()

# sleep(2)
# ele = driver.find_element(By.XPATH, "//div[contains(@class, 'a-cardui _quad-multi-asin-card-v2_fluid_fluidCard')][1]")
# actions = ActionChains(driver)
# actions.scroll_to_element(ele).perform()
# sleep(6)
# actions.scroll_by_amount(0, 5000).perform()
#
# bike = driver.find_element(By.XPATH, '(//span[@class="a-list-item"])[4]')
# origin = ScrollOrigin.from_element(bike)
#
# actions.pause(2).scroll_from_origin(origin, 0, 10000).perform()

#HOVER ACTIONS
# el = driver.find_element(By.XPATH, '//div[@class="nav-line-1-container"]')
# actions.move_by_offset(0, 800).perform()

#CLICK AND HOLD
driver.get('https://yonobusiness.sbi.bank.in/yonobusinesslogin')
driver.maximize_window()
sleep(2)
input = driver.find_element(By.ID, "password")
eye = driver.find_element(By.XPATH, '//button//img[@src="assets/img/Revamp/icon_eye_close.svg"]')
input.click()
input.send_keys("aditi")
actions = ActionChains(driver)
sleep(2)
actions.click_and_hold(eye).pause(3).release().perform()