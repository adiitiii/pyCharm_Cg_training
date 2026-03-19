from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
o.add_argument('--headless')
driver = Chrome(options=o)

driver.get('https://the-internet.herokuapp.com/tables')
name = driver.find_element(By.XPATH, '//td[text()="Tim"]//preceding-sibling::td[1]').text
print(name)