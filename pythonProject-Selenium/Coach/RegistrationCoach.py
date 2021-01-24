from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from config.config import settings
import xlrd
import time

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(2)
driver.get("http://34.199.234.160:51/Login")

class Coach_tests:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Coach_tests()
        return cls.instance

    def registration(self):
        try:
            file_path = settings['test_data_loc']
            workbook = xlrd.open_workbook(file_path)
            sheet = workbook.sheet_by_name("Coach")
            rowcount = sheet.nrows
            colcount = sheet.ncols

            for curr_row in range(1, rowcount):
                FirstName = sheet.cell_value(curr_row, 0)
                Gender = sheet.cell_value(curr_row, 1)
                Email_add = sheet.cell_value(curr_row, 2)
                Sport_sel = sheet.cell_value(curr_row, 3)

            # Click Register here
            driver.find_element_by_xpath("//a[text()='Register Here']").click()
            driver.implicitly_wait(5)
            # Click on Coach button on new registration
            driver.find_element_by_xpath("//p[text()='Coaches']").click()
            driver.find_element_by_xpath("//button[text()='Proceed']").click()
            driver.implicitly_wait(5)

            # to upload image
            driver.find_element_by_xpath("//input[@id = 'profile_image_btn']").send_keys("D:\\download.png")


            # to upload first name, mother name and father name
            driver.find_element_by_id('first_name').send_keys(FirstName)


            # to select Gender
            element_gen = driver.find_element(By.ID, 'gender')
            select = Select(element_gen)
            select.select_by_value(Gender)

            # to Select DOB
            DOB = driver.find_element_by_xpath("//input[@placeholder='Enter Date Of Birth']")
            DOB.click()
            DOB.clear()
            DOB.send_keys('10/11/2007')

            # to fill Address
            driver.find_element_by_xpath("//input[@id ='address_of_name']").send_keys('Rudra')
            driver.find_element_by_xpath("//input[@id ='post_office']").send_keys('208016')
            driver.find_element_by_xpath('//*[@id="sub_district"]').send_keys('Kanpur dehat')

            # to fill permanent address
            chk = driver.find_element_by_css_selector('#filladdress')
            chk.click()
            driver.implicitly_wait(10)

            # to fill mobile number and email id
            driver.find_element_by_xpath("//input[@id ='MobileNoUser']").send_keys('9599108494')
            email = driver.find_element_by_xpath("//input[@id = 'nsf_email_id']")
            email.send_keys(Email_add)

            # select Sport
            sports = driver.find_element_by_xpath("//select[@id = 'sport_detail_id']")
            sport = Select(sports)
            sport.select_by_value(Sport_sel)

            # select Login password
            driver.find_element_by_xpath("//input[@id = 'login_password']").send_keys('Admin@123')
            driver.find_element_by_xpath("//input[@id = 'confirm_password']").send_keys('Admin@123')

            # Click on Checkbox (Terms & Condition)
            action = ActionChains(driver)
            source = driver.find_element_by_xpath("//input[@name= 'terms_conditions']")
            action.click(source)
            action.perform()

            driver.find_element_by_xpath('//a[@id="CoachPILink"]').click()

        except Exception as e:
            print("Error while accessing page : " + str(e))
            # driver.quit()
        time.sleep(50)


Coach_test = Coach_tests.get_instance()