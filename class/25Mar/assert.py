from time import sleep
import os
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
# driver.get('https://www.google.com/')0
# driver.maximize_window()
# # print(driver.title)
#
# expexted = 'Google'
# actual = driver.title
# assert expexted == actual , 'Title mismatch'#if this fails, it will not move ahead
#
# driver.find_element(By.XPATH, '//textarea[@title="Search"]').send_keys("selenium")
# sleep(3)
# driver.close()

driver.get('https://www.amazon.in/')
driver.maximize_window()

sleep(3)
driver.find_element(By.XPATH, '//a[text()="Bestsellers"][1]').click()

sleep(3)
expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
actual = driver.title
assert expected == actual, 'title mismatch'
driver.save_screenshot('screenshot.png')

folder = os.path.join(os.getcwd(), 'screenshot')
os.mkdirs(folder, exist_ok=True)

driver.save_screenshot(f'{folder}/screenshot.png')
timestamp = time.strftime('%Y%m%d_%H%M%S')

driver.quit()


'''

#  if u want to store in differ location

import os  # if u want to store in differ location
folder=os.path.join(os.getcwd() , "screenshot")    # now this folder is created now we check if it exists or not
os.makedirs(folder,exist_ok=True)                   # this will check folder existance
#
# driver.save_screenshot(f'{folder}/screenshot.png')

# screenshot of a particular element
# ele=driver.find_element(By.XPATH,"//textarea[@title='Search']")
# ele.screenshot(f'{folder}/search.png')

#  based on time also we can store screeenshot
#  we need to import time
# multiple screenshot will not have same name
# ele2=driver.find_element(By.XPATH,"//div[@id='LS8OJ']")
import time
timestamp=time.strftime("%Y%m%d%H%M%S")
# ele2.screenshot(f'{folder}/{timestamp}.png')

ele3=driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']")
ele3.screenshot(f'{folder}/screenshot_ele3_{timestamp}.png')'''