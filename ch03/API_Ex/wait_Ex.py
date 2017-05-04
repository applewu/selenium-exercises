from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://cn.bing.com/")
driver.implicitly_wait(60)
driver.find_element_by_id("sb_form_q").send_keys("selenium")
# Should be throw timeout exception
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.TAG_NAME, 'input1')))
