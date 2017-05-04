# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
driver.get("http://mail.163.com/")
driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
driver.find_element_by_name('email').send_keys('wuziteng2006')
driver.find_element_by_name('password').send_keys('Password01!')
# driver.find_element_by_id('idInput').send_keys('wuziteng2006')
# driver.find_element_by_id('pwdInput').send_keys('Password01!')
# driver.find_element_by_id('loginBtn').click()
driver.find_element_by_id('dologin').click()

# wait = WebDriverWait(driver, 5)
# element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'spnUid')))
time.sleep(3)
driver.find_element_by_id('_mail_component_61_61').click()
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('wuziteng2006@163.com')
mail_title = u'Lettuce Selenium测试'
driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys(mail_title)

time.sleep(5)

driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[9])
mail_body = driver.find_element_by_xpath('/html/body')
ActionChains(driver).move_to_element(mail_body).send_keys(u'这是脚本发送的邮件，可以删除').perform()
# mail_body.send_keys(u'这是脚本发送的邮件，可以删除')
driver.switch_to.parent_frame()
driver.find_elements_by_class_name('nui-btn-text')[2].click()  # 发送
time.sleep(5)

driver.find_element_by_id('_mail_tabitem_3_43').click()  # 收件箱

js = '''$("span:contains('{0}')").dom.parentNode.previousElementSibling.childNodes[1].click();'''.format(mail_title)
time.sleep(3)
driver.execute_script(js)

driver.find_elements_by_class_name('nui-btn-text')[12].click()  # 删除

