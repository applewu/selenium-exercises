__author__ = 'applewu'

from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/Users/applewu/Documents/iCode/selenium/ch03/Iframe/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Iframe/iframe.html')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.find_element_by_name('sub').send_keys('1st Input')
driver.switch_to.default_content()
driver.find_element_by_name('parent').send_keys('2nd Input')
driver.maximize_window()
driver.save_screenshot('iframe_Ex.png')

