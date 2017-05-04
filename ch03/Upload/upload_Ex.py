from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("file:///Users/applewu/Documents/iCode/selenium/ch03/Upload/upload.html")
fileInput = driver.find_element_by_name('uploadfile')
fileInput.send_keys('/Users/applewu/Documents/iCode/selenium/ch03/Download/icon.png')
driver.find_elements_by_tag_name('input')[1].click()
WebDriverWait(driver, 5).until(EC.invisibility_of_element_located((By.NAME, 'uploadfile')))
assert driver.title == 'File Upload Results'
