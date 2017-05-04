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
driver.get('http://galacticmilk.com/sketchpad/')

# 截图－保存初始界面
wait = WebDriverWait(driver, 5)
element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'ctx_marquee')))
driver.save_screenshot('init_{0}.png'.format(get_time()))

# 点击左侧工具箱中的刷子，用于作画
driver.find_element_by_xpath('//*[@id="tools"]/div/div[5]/div/div[1]/div[7]').click()

# 移动鼠标作画，并截图
actions = ActionChains(driver)
actions.click_and_hold(element).move_by_offset(30, 100).move_by_offset(100, 30).move_by_offset(-30,
                                                                                               -100).move_by_offset(
    -100, -30).release().perform()
driver.save_screenshot('draw_{0}.png'.format(get_time()))

driver.quit()






