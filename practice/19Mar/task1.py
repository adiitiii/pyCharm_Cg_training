'''
PROB STATEMENT 1:
Open amazon and go to watch page while searching for it afterwards find all the images inside of it and
open the 4th image in a new tab
'''

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

driver = Chrome()
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Watch for men')
sleep(5)
results = driver.find_elements(By.CLASS_NAME,'a-section.aok-relative.s-image-tall-aspect')
print(len(results))
results[4].click()
