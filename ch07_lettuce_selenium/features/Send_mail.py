# -*- coding: utf-8 -*-
from lettuce import *
from selenium.webdriver.common.action_chains import ActionChains
import time

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


@step(u'用户使用正确的用户名(.*)密码(.*)登陆')
def logged_in(step, user_name, pwd):
    step.behave_as("""
        首先 用户访问163邮箱首页
        当 用户输入用户名{0}
        并且 用户输入密码{1}
        并且 用户点击登录按钮
        那么 用户{0}会登录成功
    """.format(user_name, pwd))


@step(u'用户点击写信按钮')
def create_new_mail(step):
    time.sleep(5)
    world.driver.find_element_by_id('_mail_component_61_61').click()


@step(u'输入当前用户的邮箱地址，作为收件人地址')
def create_new_mail(step):
    world.driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('wuziteng2006@163.com')


@step(u'输入邮件主题为(.*)')
def create_new_mail(step, mail_title):
    world.driver.find_elements_by_class_name('nui-ipt-input')[2].send_keys(mail_title)
    time.sleep(5)


@step(u'输入邮件正文(.*)')
def create_new_mail(step, mail_body):
    world.driver.switch_to.frame(world.driver.find_elements_by_tag_name("iframe")[9])
    body_element = world.driver.find_element_by_xpath('/html/body')
    ActionChains(world.driver).move_to_element(body_element).perform()
    body_element.send_keys(mail_body)
    world.driver.switch_to.parent_frame()


@step(u'点击发送按钮')
def create_new_mail(step):
    world.driver.find_elements_by_class_name('nui-btn-text')[2].click()  # 发送


@step(u'页面提示发送成功')
def assert_sent(step):
    world.driver.save_screenshot('sent_mail.png')

