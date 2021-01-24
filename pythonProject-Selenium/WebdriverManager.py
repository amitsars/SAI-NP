from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browsername = "chrome"

if browsername == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif browsername == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
else:
    print("Correct browser should be : " + browsername)
    raise Exception ('please select correct browser')

driver.implicitly_wait(10)
driver.get("http://34.199.234.160:51/")
driver.find_element(By.ID, 'username').send_keys("OPSUser")
driver.find_element(By.ID, 'Password').send_keys("OPSUser")
driver.find_element(By.ID, 'login-button').click()

time.sleep(10)
driver.quit()

