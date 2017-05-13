__author__ = 'applewu'

"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from random import randint
from appium import webdriver
from time import sleep

class MoviesIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        app = '/Applications/Movies.app'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.3',
                'deviceName': 'iPhone 6'
            })

    def tearDown(self):
        # self.driver.quit()
        self.driver.close_app()

    # def test_item_details(self):
    #     pass

    def test_search(self):
        query_element = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
        query_element.send_keys('Bad Moms')
        first_item = self.driver.find_element_by_xpath('//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIAElement[1]')
        assert str(first_item.get_attribute('name')) == '   Bad Moms 2016 • Critics 63%'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MoviesIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

