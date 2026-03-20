from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get('https://www.shine.com/registration/')
driver.maximize_window()

wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.ID, "id_file"))).send_keys(r"C:\Users\adima\OneDrive\Desktop\Aditi_Credentials\Aditi Maheshwari Resume.pdf")
sleep(5)
driver.quit()