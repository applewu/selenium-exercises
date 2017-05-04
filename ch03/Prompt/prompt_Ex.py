from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Prompt/prompt.html')
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'alert')))
driver.find_element_by_class_name('alert').click()
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, 'input')))
driver.find_element_by_tag_name('input').send_keys('Tester')
driver.find_element_by_tag_name('input').send_keys(Keys.ENTER)
driver.quit()
