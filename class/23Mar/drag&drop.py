from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/droppable")
driver.maximize_window()
el1 = driver.find_element(By.ID, "droppable")
el2 = driver.find_element(By.ID, "draggable")
actions = ActionChains(driver)
sleep(3)
actions.drag_and_drop(el2, el1).perform()