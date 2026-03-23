from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# o =ChromeOptions()
# o.add_experimental_option('detach', True)
# driver = Chrome(options=o)
# driver.get('file:///C:/Users/adima/AppData/Local/Packages/5319275A.WhatsAppDesktop_cv1g1gvanyjgm/LocalState/sessions/2EDAC5EA4DA4AB1C20BD68C4008819E32615A112/transfers/2026-12/E22_Dropdowns.html')
# driver.maximize_window()

# dropdown = driver.find_element(By.ID, 'state')
# option = Select(dropdown) #here option is an object
# option.select_by_value('MH')
# sleep(3)
# # option.select_by_visible_text('Maharastra')
# option.select_by_index(1)

# d1 = driver.find_element(By.ID, "hobby")
# option = Select(d1)
# option.select_by_index(1)
# sleep(2)
# option.select_by_index(2)
# sleep(2)
# option.select_by_index(4)
# #In multi select we can deselect it also according to our wish
# option.deselect_by_index(1)
# sleep(2)
# option.deselect_by_index(2)
# sleep(2)
# option.deselect_by_index(3)

#CUSTOM DROPDOWN
