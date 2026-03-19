from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome()
driver.get('https://www.google.com')
driver.maximize_window()
driver.implicitly_wait(10)
# driver.find_element(By.TAG_NAME, 'a').click() here first linked page is getting clicked
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    print(link.text)
print(len(links))
driver.quit()