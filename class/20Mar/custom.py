from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.amazon.in/')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, 'twotabsearchtextbox').click()
sleep(2)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shoes')
sleep(2)
eles = driver.find_elements(By.XPATH, '//div[@class="s-suggestion-container"]')
for e in eles:
    print(e.text)
sleep(2)
eles[8].click()