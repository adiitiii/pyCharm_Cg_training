'''
TASK1

https://testautomationpractice.blogspot.com/
->mouse hover on
->double click action on copy text below it
->drag and drop

all using action chains

flipakrt, scroll to last, footer click on myntra from new tab switch to flipkart click on shopsy, then fetch all window IDs, title, url for all tabs opened
'''


from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = ChromeOptions()
options.add_experimental_option("detach", True)
driver = Chrome(options=options)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()

#ACTION CHAINS
actions = ActionChains(driver)

#MOUSE HOVER
hover = driver.find_element(By.XPATH, '//button[text()="Point Me"]')
sleep(2)
actions.move_to_element(hover).perform()

#DOUBLE CLICK ACTION
dblClick = driver.find_element(By.XPATH, '//button[text()="Copy Text"]')
sleep(2)
actions.double_click(dblClick).perform()

#DRAG & DROP ACTION
src = driver.find_element(By.ID, 'draggable')
dest = driver.find_element(By.ID, 'droppable')
sleep(2)
actions.drag_and_drop(src, dest).perform()

driver.quit()