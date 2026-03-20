from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.get("https://www.prokabaddi.com/")

driver.maximize_window()
sleep(2)
driver.implicitly_wait(10)

driver.find_element(By.XPATH,"//span[text()='Standings']").click()
name = driver.find_element(By.XPATH,"(//div[@class='table-data team'])[9]//div[2]").text
matches = driver.find_element(By.XPATH,"(//p[@class='count'])[36]")
won = driver.find_element(By.XPATH,"(//p[@class='count'])[37]")
lost = driver.find_element(By.XPATH,"(//p[@class='count'])[38]")
sd = driver.find_element(By.XPATH,"(//p[@class='count'])[39]")
points = driver.find_element(By.XPATH,"(//p[@class='count'])[40]")

print("Matches Played:" + matches.text)
print("Won:" + won.text)
print("Lost:" + lost.text)
print("Score difference:" + sd.text)
print("Points:" + points.text)
driver.quit()