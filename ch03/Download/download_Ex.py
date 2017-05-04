__author__ = 'applewu'

from selenium import webdriver
import urllib
import os

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Download/download.html')
downloadFile_url = driver.find_element_by_id('fileToDownload').get_attribute('href')
file_name = 'test.zip'
urllib.urlretrieve(downloadFile_url, file_name)
# Check if the file existed in the folder yet
current_path = os.path.split(os.path.realpath(__file__))[0]
assert os.path.isfile('{0}/{1}'.format(current_path, file_name)) is True
driver.quit()