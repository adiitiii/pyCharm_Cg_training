from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nw1UBF.v1zwn25"))).click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "nw1UBF.v1zwn25"))).send_keys("Mobiles")
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "XFwMiH"))).click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "lvJbLV.col-12-12"[6]))).click()