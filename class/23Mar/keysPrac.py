from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://demoqa.com/text-box")
ele = driver.find_element(By.ID, "currentAddress")
ele.click()
ele.send_keys("F-2 Raghukul App, Vaishali Nagar")
ele.send_keys(Keys.CONTROL, "a")
ele.send_keys(Keys.CONTROL, "c")
ele2 = driver.find_element(By.ID, "permanentAddress")
ele2.click()
ele2.send_keys(Keys.CONTROL, "v")