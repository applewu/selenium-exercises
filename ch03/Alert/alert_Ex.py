from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Alert/alert.html')
# driver.get('http://bootboxjs.com/examples.html#')
# driver.find_elements_by_class_name('btn btn-default')[0].click()
driver.find_element_by_tag_name('input').click()
# Alert(driver).accept()
Alert(driver).dismiss()
driver.quit()