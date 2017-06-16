__author__ = 'applewu'

# -*- encoding:utf8 -*-
from selenium import webdriver
import urllib.request
import os

driver = webdriver.Firefox()
driver.get('file:///d:/iCode/iGithub/selenium-exercises/ch03/Download/download.html')
downloadFile_url = driver.find_element_by_id('fileToDownload').get_attribute('href')
file_name = 'test.zip'
# 使用 urllib 模块的方法，将文件下载到本地，命名为 test.zip
urllib.request.urlretrieve(downloadFile_url, file_name)
# 获得当前脚本的所在目录
current_path = os.path.split(os.path.realpath(__file__))[0]
# 检查当前目录中是否存在名为 test.zip 的文件
assert os.path.isfile('{0}/{1}'.format(current_path, file_name)) is True
driver.quit()