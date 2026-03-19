from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC #EC is alias name

o =ChromeOptions()
o.add_experimental_option('detach', True)
# var = o.headless
driver = Chrome(options=o)


driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')

driver.maximize_window()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//button[text()='Start']").click()
print(wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@id="finish"]'))).text)

