from selenium.webdriver.common.by import By

from POm.basepage import BasePage


class LoginPage(BasePage):
    __username = (By.ID, "username")
    __password = (By.NAME, "pwd")
    __login = (By.XPATH,"//div[.='Login ']")

    def __init__(self, driver):
        self.driver = driver

    def set_username(self,uname):
        self.driver.find_element(*self.__username).send_keys(uname)

    def set_password(self,pword):
        self.driver.find_element(*self.__password).send_keys(pword)

    def click_login(self):
        self.driver.find_element(*self.__login).click()



