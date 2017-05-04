# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time


# 获得当前时间
def get_time():
    return time.strftime("%Y%m%d%H%M%S", time.localtime())

driver = webdriver.Firefox()
driver.get('https://cdn.sencha.com/touch/sencha-touch-2.4.1/examples/stockapp/index.html')

# 截图－保存初始图形
wait = WebDriverWait(driver, 5)
element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'ext-element-33')))
driver.save_screenshot('1_{0}.png'.format(get_time()))

driver.mobile.set_network_connection()
#
left_element = driver.find_element_by_id('ext-element-33')
right_element = driver.find_element_by_id('ext-element-55')
actions = ActionChains(driver)
actions.click_and_hold().move_by_offset(800, 0).release().perform()
# ActionChains(driver).drag_and_drop(left_element, right_element).perform()
# actions.perform()
# time.sleep(2)
driver.save_screenshot('2_{0}.png'.format(get_time()))

# 单击 OHLC 按钮
# driver.find_element_by_id('ext-element-20').click()
# actions.click_and_hold(left_element).move_by_offset(800, 0).release().perform()
# actions.perform()
# time.sleep(2)
# driver.save_screenshot('3_{0}.png'.format(get_time()))
# driver.close()
