from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

o = ChromeOptions()
o.add_experimental_option("detach", True)
# o.add_experimental_option("prefs", {'safebrowsing.enabled':True}) #telling it that theres an authorised person trying to download
o.add_argument("--disable-notifications") #unwanted notifications wont come
driver = Chrome(options=o)
actions = ActionChains(driver)

driver.get('https://www.irctc.co.in/nget/train-search')
driver.maximize_window()
sleep(4)

inputDate = driver.find_element(By.XPATH, '//input[@class="ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted"]')
inputDate.click()
sleep(2)

next_el = driver.find_element(By.XPATH, '//span[@class="ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9"]')
actions.double_click(next_el).perform()

driver.find_element(By.XPATH, '//a[text()="26"]').click()

driver.quit()