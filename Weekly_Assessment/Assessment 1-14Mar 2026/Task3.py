from selenium.webdriver import Chrome, ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o= ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.myntra.com")
driver.maximize_window()
driver.find_element(By.CLASS_NAME,"desktop-searchBar").send_keys("shoes")

sleep(2)
driver.quit()