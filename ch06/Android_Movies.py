__author__ = 'applewu'

"""
Simple iOS tests, showing accessing elements and getting/setting text from them.
"""
import unittest
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from appium import webdriver


class MoviesIOSTests(unittest.TestCase):

    def setUp(self):
        # set up appium
        dir_path = os.path.dirname(os.path.realpath(__file__))
        app = dir_path + '/apps/Movies.apk'
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '4.4',
                'deviceName': 'Genymotion Emulator'
            })
        self.driver.scroll()
    def tearDown(self):
        self.driver.quit()
        # self.driver.close_app()

    def test_search(self):

        # Wait for the query element
        WebDriverWait(self.driver, 8).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'android.widget.EditText')))

        query_element = self.driver.find_element_by_class_name('android.widget.EditText')
        query_element.send_keys('Bad Moms')
        first_item = self.driver.find_element_by_class_name('android.widget.TextView')
        assert str(first_item.get_attribute('text')) == 'Bad Moms'


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MoviesIOSTests)
    unittest.TextTestRunner(verbosity=2).run(suite)

