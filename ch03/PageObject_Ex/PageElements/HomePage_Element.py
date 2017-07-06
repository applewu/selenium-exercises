__author__ = 'applewu'

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class HomePage_Element(object):

    txt_query = (By.NAME, "q")

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)