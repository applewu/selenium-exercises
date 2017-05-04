# -*- coding: utf-8-*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/PopUp/popUp.html')
driver.find_element_by_tag_name('input').click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_class_name('input-group-field').send_keys(u'渠道')
driver.find_element_by_link_text(u'搜索').click()
driver.quit()


driver.switch_to.parent_frame()