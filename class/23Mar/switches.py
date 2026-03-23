'''
TAB AND WINDOW HANDLING
to switch the driver control of tab from one tab to another
current_window_handle -> fetches the current window handle ID
window_handles -> gives a list of multiple tabs opened
switch_to_window(destination window)
'''

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.google.com/?zx=1774263346997&no_sw_cr=1")
driver.maximize_window()
sleep(5)
#Manually opened three tabs
current_tab = driver.current_window_handle
print(driver.title)
print(current_tab)
# all_tabs = driver.window_handles
#to open multiple tabs automatically
driver.switch_to.new_window()
driver.get("https://www.amazon.in/")
sleep(2)
print(driver.title)
print(driver.current_window_handle)
sleep(8)
driver.switch_to.window(driver.window_handles[0])
sleep(5)
print(driver.title)

# print(all_tabs)
