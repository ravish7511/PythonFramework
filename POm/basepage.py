import logging
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_logger(self):
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def verity_title(self, title):
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.title_contains(title))

    def mouse_hover(self, element):
        act = ActionChains(self.driver)
        act.move_to_element(self, element).perform()

    def select_value_from_dropdown(self, element, value):
        s1 = Select(element)
        s1.select_by_value(value)
