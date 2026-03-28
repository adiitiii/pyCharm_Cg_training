from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)

driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, '//ul[@class="top-menu"]//li[4]').click()
dropdown1 = driver.find_element(By.XPATH, '//select[@id="products-orderby"]')
option = Select(dropdown1)
option.select_by_value('https://demowebshop.tricentis.com/apparel-shoes?orderby=5')
sleep(2)
dropdown2 = driver.find_element(By.XPATH, '//select[@id="products-pagesize"]')
option = Select(dropdown2)
option.select_by_index(2)
sleep(2)
dropdown3 = driver.find_element(By.XPATH, '//select[@id="products-viewmode"]')
option = Select(dropdown3)
option.select_by_visible_text('List')