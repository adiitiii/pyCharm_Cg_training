from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get('https://www.wikipedia.org/')
sleep(3)
driver.refresh()
sleep(3)
print(driver.title)
sleep(3)
driver.get('https://www.amazon.in/')
print(driver.title)
sleep(3)
driver.back()
sleep(3)
driver.quit()
