# -*- coding: utf-8 -*-
__author__ = 'applewu'

from lettuce import step
from lettuce import world
import time

@step(u'发送一封主题为(.*)的邮件给自己')
def send_mail(step, mail_title):
    step.behave_as("""
        首先 用户使用正确的用户名hellotester@163.com密码xxxxxxxxxxxx登陆
        当 用户点击写信按钮
        并且 输入当前用户的邮箱地址，作为收件人地址
        并且 输入邮件主题为{0}
        并且 输入邮件正文 这是脚本发送的邮件，可以删除
        并且 点击发送按钮
        那么 页面提示发送成功
    """.format(mail_title))

@step(u'用户进入收件箱')
def access_inbox(step):
    world.driver.find_element_by_id('_mail_tabitem_3_43').click()


@step(u'勾选邮件标题为(.*)前方的多选框')
def select_mail(step, mail_title):
    print mail_title
    js = '''$("span:contains('{0}')").dom.parentNode.previousElementSibling.childNodes[1].click();'''.format(mail_title)
    time.sleep(3)
    world.driver.execute_script(js)


@step(u'点击删除按钮')
def del_mail(step):
    world.driver.find_elements_by_class_name('nui-btn-text')[12].click()


@step(u'页面提示删除成功')
def assert_del(step):
    world.driver.save_screenshot('deleted_mail.png')

