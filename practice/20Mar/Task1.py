from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions

option = ChromeOptions()
option.add_experimental_option('detach', True)
driver = Chrome(options=option)
driver.maximize_window()
driver.get('https://www.zomato.com/jaipur/restaurants')
sleep(2)

driver.find_element(By.XPATH, '//input[@placeholder="Search for restaurant, cuisine or a dish"]').send_keys("waffles")
driver.find_element(By.XPATH, '//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
sleep(2)
eles = driver.find_elements(By.XPATH, '//div[@class="sc-glUWqk GrjUP"]')
for e in eles:
    print(e.text)
sleep(2)
eles[0].click()