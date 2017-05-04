# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Hover/hoverMenu.html')
menu = driver.find_element_by_id('menuitems')
menu_item = driver.find_element_by_xpath('//*[@id="menuitems"]/ul/li[2]/a')
# ActionChains(driver).move_to_element(menu).move_to_element(menu_item).click().perform()
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'logo')))
# assert driver.title == u'API 参考 | 为开发者设计的支付聚合 SDK'
# driver.quit()

menu_item.click()
