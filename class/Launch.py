from time import sleep

'''
from selenium.webdriver import Edge
driver = Edge() #Object creation
#sleep(5) #holding the screen
'''

from selenium.webdriver import Chrome, ChromeOptions
o =ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o) #Object creation

#to open a webpage, get method return type is none
# driver.get('https://demoqa.com/')

#to maximize it, maximize_window method return type is none
# driver.maximize_window()
# sleep(5)
# driver.minimize_window()
# sleep(5)
# driver.fullscreen_window() #all the taskbar and tabs are gone


# to fetch the title of webpage, return type is string and title, url are a verification "property"
# to fetch the title of webpage, return type is string and title, url are a verification "property"
# title = driver.page_source  #give the source code of html
# print(title)
# title = driver.title
# url = driver.current_url
# page_s = driver.page_source
# print(title)
# print(url)
# print(page_s)
# print(driver.name)
# sleep(7)
# driver.close() #only yhe specific tab opened by the selenium
# driver.quit() #all yhe chrome window will shut down automatically

'''
Driver is a variable which is holding the opened browser
add_experimental_option : extra browser setting
sleep is used to pause the execution of the program for a particular seconds of time
to fetch the title of webpage: title and its not a method but a property url and page_source are also in the same line
Page Information Properties: title, url, page_source
'''

# Back, forward, Refresh
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(3) ##navigate to any one page
print(driver.title)
driver.back()
print(driver.title)
sleep(3)
driver.forward()
print(driver.title)
sleep(3)
driver.refresh()
