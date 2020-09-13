from selenium.webdriver.common.by import By

from POm.basepage import BasePage


class HomePage(BasePage):
    __logout = (By.ID, "logoutLink")

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(*self.__logout).click()