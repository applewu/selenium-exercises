__author__ = 'applewu'

from PageElements import HomePage_Element


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class HomePage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "GitHub" in self.driver.title

    def enter_query_txt(self, value):
        """Triggers the search"""
        element = self.driver.find_element(HomePage_Element.HomePage_Element.txt_query)
        element.send_keys(value)