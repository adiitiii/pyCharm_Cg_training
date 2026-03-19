from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.amazon.in/')
sleep(3)
driver.find_element(By.ID, "twotabsearchtextbox").send_keys('Mobiles')
driver.find_element(By.ID, "nav-search-submit-button").click()
driver.find_element(By.XPATH, '//h2[contains(@aria-label, "iPhone 17")]').click()
print(driver.find_element(By.XPATH, '//span[@class="a-price-whole"]').text)