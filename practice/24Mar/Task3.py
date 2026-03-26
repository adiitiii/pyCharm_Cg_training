'''
open any 3 websites in separate tabs print each tab's title n url, close all except first tab

'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demoqa.com/")
driver.maximize_window()
driver.implicitly_wait(10)

print(f"Name: {driver.title}, URL : {driver.current_url}")

driver.switch_to.new_window()
driver.get('https://www.cult.fit/')
print(f"Name: {driver.title}, URL : {driver.current_url}")

driver.switch_to.new_window()
driver.get('https://www.theodinproject.com/')
print(f"Name: {driver.title}, URL : {driver.current_url}")

cls = driver.window_handles
for c in cls[1:]:
    driver.switch_to.window(c)
    driver.close()

