__author__ = 'applewu'

import unittest
from selenium import webdriver
import page


class GitHubSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://github.com/")

    def test_search_in_python_org(self):

        #Load the home page. In this case the home page of github.com.
        home_page = page.HomePage(self.driver)
        #Checks if the word "GitHub" is in title
        assert home_page.is_title_matches(), "github.com title doesn't match."
        #Sets the text of search textbox to "pingplusplus"
        home_page.enter_query_txt('pingplusplus')
        # search_results_page = page.SearchResultsPage(self.driver)
        # #Verifies that the results page is not empty
        # assert search_results_page.is_results_found(), "No results found."

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()