from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()
driver.get("http://cn.bing.com/")
driver.find_element_by_id("sb_form_q").send_keys("selenium")
driver.find_element_by_id("sb_form_go").click()
# driver.find_element(by=By.ID, "sb_form_q")