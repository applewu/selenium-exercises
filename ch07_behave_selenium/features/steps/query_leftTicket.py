# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
import time
import sys

reload(sys)
sys.setdefaultencoding("utf-8")


@given(u'访问余票查询页面')
def visit_left_ticket(context):
    context.driver.get("https://kyfw.12306.cn/otn/lcxxcx/init")


@when(u'用户先输入{from_station}')
def enter_from_station_name(context, from_station):
    from_station_element = context.driver.find_element_by_id('fromStationText')
    from_station_element.clear()
    ActionChains(context.driver).click(from_station_element).send_keys(from_station)
    ActionChains(context.driver).click(from_station_element).send_keys(Keys.DOWN)
    ActionChains(context.driver).click(from_station_element).send_keys(Keys.ENTER).perform()


@when(u'用户再输入{to_station}')
def enter_to_station_name(context, to_station):
    to_station_element = context.driver.find_element_by_id('toStationText')
    to_station_element.clear()
    ActionChains(context.driver).click(to_station_element).send_keys(to_station)
    ActionChains(context.driver).click(to_station_element).send_keys(Keys.DOWN)
    ActionChains(context.driver).click(to_station_element).send_keys(Keys.ENTER).perform()


@when(u'用户点击查询按钮')
def submit(context):
    context.driver.find_element_by_id('_a_search_btn1').click()


@when(u'用户点击查询学生票按钮')
def submit_stu(context):
    context.driver.find_element_by_id('_a_search_btn2').click()


@given(u'用户已查询到从{from_station}到{to_station}的车次信息')
def get_train_yet(context, from_station, to_station):
    context.execute_steps(u'''
        假如 访问余票查询页面
        当 用户先输入{0}
        而且 用户再输入{1}
        而且 用户点击查询按钮
        那么 页面显示车次信息
    '''.format(from_station, to_station))

@when(u'用户输入车次{train_no}')
def enter_train_no(context, train_no):
    train_no_element = context.driver.find_element_by_id('train_combo_box')
    # ActionChains(context.driver).click(train_no_element).send_keys(train_no).perform()
    train_no_element.send_keys(train_no)

@then(u'页面显示车次信息')
def appear_list(context):
    time.sleep(3)

    # 若没有弹出“没有符合条件的数据”的提示，则说明查询到了车次信息，列表中的子节点数目大于零
    result = context.driver.execute_script('''return $("div:contains('content_defaultwarningAlert_hearder')")''')
    if result.__len__() == 0:
        train_count = context.driver.execute_script('return document.getElementById("_query_table_datas").childNodes.length')
        assert train_count > 0
