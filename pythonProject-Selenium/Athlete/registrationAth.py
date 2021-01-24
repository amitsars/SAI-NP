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

class Athletes_tests:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Athletes_tests()
        return cls.instance

    def registration(self):
        try:
            file_path = settings['test_data_loc']
            workbook = xlrd.open_workbook(file_path)
            sheet = workbook.sheet_by_name("Athlete")
            rowcount = sheet.nrows
            # colCount = sheet.ncols

            for curr_row in range(1, rowcount):
                FirstName = sheet.cell_value(curr_row, 0)
                MotherName = sheet.cell_value(curr_row, 1)
                FatherName = sheet.cell_value(curr_row, 2)
                Gender = sheet.cell_value(curr_row, 3)
                Email_add = sheet.cell_value(curr_row, 4)
                Sport_sel = sheet.cell_value(curr_row, 5)

            # Click Register here
            driver.find_element_by_xpath("//a[text()='Register Here']").click()
            driver.implicitly_wait(5)
            # Click on Athlete button on new registration
            driver.find_element_by_xpath("//p[text()='Athletes']").click()
            driver.find_element_by_xpath("//button[text()='Proceed']").click()
            driver.implicitly_wait(5)

            # to upload image
            driver.find_element_by_id('profile_image_btn').send_keys("D:\\download.png")

            # to upload first name, mother name and father name
            driver.find_element_by_id('first_name').send_keys(FirstName)
            mother_name = driver.find_element_by_id('mother_full_name')
            mother_name.send_keys(MotherName)
            father_name = driver.find_element_by_id('father_full_name')
            father_name.send_keys(FatherName)

            # to select Gender
            element_gen = driver.find_element(By.ID, 'gender')
            select = Select(element_gen)
            select.select_by_value(Gender)
            # select.select_by_visible_text('Male')
            # select.select_by_index(2)
            # select.select_by_value('F')

            # to Select DOB
            DOB = driver.find_element_by_xpath("//input[@placeholder='Enter Date Of Birth']")
            DOB.click()
            DOB.clear()
            DOB.send_keys('04/10/2018')

            # to fill Address
            driver.find_element_by_xpath("//input[@id ='address_of_name']").send_keys('Rohit')
            driver.find_element_by_xpath("//input[@id ='post_office']").send_keys('742101')
            driver.find_element_by_xpath('//*[@id="sub_district"]').send_keys('sub')

            # to fill permanent address
            chk = driver.find_element_by_css_selector('#filladdress')
            chk.click()
            driver.implicitly_wait(10)

            # to fill mobile number and email id
            driver.find_element_by_xpath("//input[@id ='MobileNoUser']").send_keys('9599108494')
            email = driver.find_element_by_xpath("//input[@id ='email_id']")
            email.send_keys(Email_add)

            # select Sport
            sports = driver.find_element_by_xpath("//select[@id ='DDLSports']")
            sport = Select(sports)
            sport.select_by_value(Sport_sel)

            # select Tracksuit
            tracksuit = driver.find_element_by_xpath("//select[@id ='blazer_size']")
            blazer = Select(tracksuit)
            blazer.select_by_visible_text('44')

            trackshirt = driver.find_element_by_xpath("//select[@id ='tshirt_size']")
            shirt = Select(trackshirt)
            shirt.select_by_visible_text('40')

            trackpant = driver.find_element_by_xpath("//select[@id ='pant_size']")
            pant = Select(trackpant)
            pant.select_by_visible_text('52')

            shoesize = driver.find_element_by_xpath("//select[@id ='shoe_size']")
            shoe = Select(shoesize)
            shoe.select_by_visible_text('10')

            # select Login password
            driver.find_element_by_xpath("//input[@id = 'login_password']").send_keys('Admin@123')
            driver.find_element_by_xpath("//input[@id = 'confirm_password']").send_keys('Admin@123')

            # Click on Checkbox (Terms & Condition)
            action = ActionChains(driver)
            source = driver.find_element_by_xpath("//input[@name= 'terms_conditions']")
            action.click(source)
            action.perform()

            driver.find_element_by_xpath('//a[@id="AthletePILink"]').click()
            # output = driver.find_element_by_xpath("//div[@class ='col-6 block block-2']//div[@class ='label-user']//span")
            # KID = output.text
            # print(KID)
            KID = driver.find_element_by_css_selector('.block-2 ')
            kid = KID.text
            print(kid)

        except Exception as e:
            print("Error while accessing page : " + str(e))
            # driver.quit()


        time.sleep(20)
        # driver.quit()


Athletes_tests = Athletes_tests.get_instance()