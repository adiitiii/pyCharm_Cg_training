from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

'''
While working with iframes it gives NoSuchElementException because 1. locator is correct or not 2. if page is loading slower n selenium is wokring fast
3. means its i frame diver control is in main frame only

to switch b/w frames
1. index
2. name
3. web element (locator)

driver.switch_to.frame(0)
'''
o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("http://127.0.0.1:5500/waste.htm")
driver.maximize_window()

sleep(2)

#WEB ELEMENT
driver.find_element(By.ID, "inp1").send_keys("first input")
ip1 = driver.find_element(By.XPATH, '//iframe[@src="waste2.htm"]')
driver.switch_to.frame(ip1)
driver.find_element(By.ID, "inp2").send_keys("second input")
ip2 = driver.find_element(By.XPATH, '//iframe[@src="waste3.htm"]')
driver.switch_to.frame(ip2)
ip3 = driver.find_element(By.ID, "inp3").send_keys("third input")

#from third input to the second input
# driver.switch_to.parent_frame()
# driver.find_element(By.ID, "inp2").clear()
# driver.find_element(By.ID, "inp2").send_keys("back to inp2")
#
# driver.switch_to.parent_frame()
# driver.find_element(By.ID, "inp1").clear()
# driver.find_element(By.ID, "inp1").send_keys("back to inp1")

driver.switch_to.default_content()
driver.find_element(By.ID, "inp1").clear()
driver.find_element(By.ID, "inp1").send_keys("back to inp1")