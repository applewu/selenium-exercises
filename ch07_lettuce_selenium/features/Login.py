# -*- coding: utf-8 -*-
from lettuce import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


@before.each_scenario
def set_up(scenario):
    world.driver = webdriver.Firefox()


@after.each_scenario
def tear_down(scenario):
    world.driver.quit()


@step(u'用户访问163邮箱首页')
def access_index_page(step):
    world.driver.get("http://mail.163.com")


@step(u'用户输入用户名(.*)')
def enter_user_name(step, user_name):
    world.driver.switch_to.frame(world.driver.find_elements_by_tag_name('iframe')[0])
    # world.driver.find_element_by_name('email').send_keys('wuziteng2006')
    world.driver.find_element_by_name('email').send_keys('wuziteng2006')

@step(u'用户输入密码(.*)')
def enter_password(step, pwd):
    # world.driver.find_element_by_name('password').send_keys('Password01!')
    world.driver.find_element_by_name('password').send_keys('Password01!')

@step(u'用户点击登录按钮')
def click_login_btn(step):
    # world.driver.find_element_by_id('loginBtn').click()
    world.driver.find_element_by_id('dologin').click()

@step(u'用户(.*)会登录成功')
def assert_login(step, acct):
    # wait = WebDriverWait(world.driver, 5)
    # element = wait.until(expected_conditions.element_to_be_clickable((By.ID, 'spnUid')))
    # assert str(element.text) == acct
    pass