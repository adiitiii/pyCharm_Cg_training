from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

sleep(2)
driver.find_element(By.ID, 'dateOfBirthInput').click()
driver.find_element(By.XPATH, '//select[@class="react-datepicker__month-select"]').click()
sleep(2)
driver.find_element(By.XPATH, '//option[@value="6"]').click()
driver.find_element(By.XPATH, '//select[@class="react-datepicker__year-select"]').click()
sleep(2)
driver.find_element(By.XPATH, '//option[@value="2003"]').click()
driver.find_element(By.CLASS_NAME, 'react-datepicker__day.react-datepicker__day--022').click()

driver.quit()