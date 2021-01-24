from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Amit\\Documents\\Selenium driver\\chromedriver.exe")
driver.implicitly_wait(5)
driver.get("http://34.199.234.160:51/")

driver.find_element(By.NAME, 'username' ).send_keys("OPSUser")

print(driver.title)
