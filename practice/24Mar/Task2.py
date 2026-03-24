from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

driver.find_element(By.XPATH, '//a[text()="Log in"]').click()
sleep(2)
frame_1 = driver.find_element(By.XPATH,'//iframe[@id="auth-login-ui"]')
driver.switch_to.frame(frame_1)
frame_2 = driver.find_element(By.XPATH,'//iframe[@title="Sign in with Google Button"][1]')
frame_2.click()