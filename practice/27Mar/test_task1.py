from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

options = ChromeOptions()
options.add_experimental_option('detach', True)
driver = Chrome(options=options)
driver.get('https://demowebshop.tricentis.com/')
driver.maximize_window()
sleep(4)

def testRegisterClick():
    driver.find_element(By.CLASS_NAME, 'ico-register').click()
    sleep(2)

def testGenderClick():
    driver.find_element(By.ID, 'gender-female').click()

def testfirstName():
    driver.find_element(By.XPATH, '//input[@id="FirstName"]').send_keys('Aditi')

def testLastName():
    driver.find_element(By.XPATH, '//input[@id="LastName"]').send_keys('Maheshwari')

def testEmail():
    driver.find_element(By.XPATH, '//input[@id="Email"]').send_keys('adi@gmail.com')

def testPassword():
    driver.find_element(By.XPATH, '//input[@id="Password"]').send_keys('adi123')

def testConfirmPassword():
    driver.find_element(By.XPATH, '//input[@id="ConfirmPassword"]').send_keys('adi123')

def testSubmit():
    driver.find_element(By.XPATH, '//input[@id="register-button"]').click()

