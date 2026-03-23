'''
TASK3

Open flipkart, scroll to last till footer click on myntra from new tab switch to flipkart again
click on shopsy,
again then fetch all window IDs, title, url for all tabs opened

'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

driver.get('https://www.flipkart.com/')
driver.maximize_window()
actions = ActionChains(driver)
sleep(5)
footer = driver.find_element(By.XPATH, '//div[text()="GROUP COMPANIES"]')
actions.scroll_to_element(footer).perform()

print("Before switching to myntra:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " First Tab Opened: ", driver.current_window_handle)

sleep(2)
myntra = driver.find_element(By.XPATH, '//a[text()="Myntra"]')
actions.click(myntra).perform()
sleep(2)

print("After switching to myntra:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " Tab Opened: ", driver.current_window_handle)

driver.switch_to.window(driver.window_handles[0])

print("Coming back to flipkart from myntra:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " Tab Opened: ", driver.current_window_handle)

cleartrip = driver.find_element(By.XPATH, '//a[text()="Cleartrip"]')
actions.click(cleartrip).perform()
sleep(2)

print("After switching to cleartrip:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " Tab Opened: ", driver.current_window_handle)


driver.switch_to.window(driver.window_handles[0])

print("Coming back to flipkart from cleartrip:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " Tab Opened: ", driver.current_window_handle)

shopsy = driver.find_element(By.XPATH, '//a[text()="Shopsy"]')
actions.click(shopsy).perform()
sleep(2)

print("After switching to shopsy:  ", "Tab Name: ", driver.title, " Tab URL: ", driver.current_url, " Tab Opened: ", driver.current_window_handle)
print("All tabs opened: ", driver.window_handles)
