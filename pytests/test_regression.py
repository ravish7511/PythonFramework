import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from DDT import excel
from POm.loginpage import LoginPage
from time import sleep
import allure

file_path = "C:\\Users\\Ravisha\\Desktop\\testdata.xlsx";


@pytest.mark.usefixtures("setup")  # cls.driver
class Test_RT:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        uname = excel.get_data(file_path, 'Sheet1', 0, 'Username')
        pword = excel.get_data(file_path, 'Sheet1', 0, 'Password')
        expected_result = excel.get_data(file_path, 'Sheet1', 0, 'Expected_Result')
        lp = LoginPage(self.driver)
        log = lp.get_logger()
        lp.set_username(uname)
        log.info('entered username')
        lp.set_password(pword)
        log.info('entered password')
        lp.click_login()
        log.info('clicked on login')
        lp.verity_title("Enter")
        actual_title = self.driver.title
        assert actual_title == expected_result
        log.info('test case executed ended')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_invalid_login(self):
        try:
            uname = excel.get_data(file_path, 'Sheet1', 1, 'Username')
            pword = excel.get_data(file_path, 'Sheet1', 1, 'Password')
            expected_result = excel.get_data(file_path, 'Sheet1', 1, 'Expected_Result')
            lp = LoginPage(self.driver)
            log = lp.get_logger()
            lp.set_username(uname)
            log.info(" username entered successfully")
            lp.set_password(pword)
            log.info("password entered successfully")
            lp.click_login()
            log.info("clicked on login")
            atitle=self.driver.title
            assert atitle == expected_result
        except Exception:
            allure.attach(self.driver.get_screenshot_as_png(),
                          name="invalid_login", attachment_type=AttachmentType.PNG)
            assert False
