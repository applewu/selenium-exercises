# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://html5demos.com/storage-events')

# 对文本框赋值，该页面程序会把这个值作为 local storage 存储
driver.find_element_by_id('data').send_keys('selenium_testing')

# 获得第一个 local storage 的值, 对于该程序而言，也是唯一一个值
value = driver.execute_script("return localStorage.getItem(localStorage.key(0));")
print('The value is: ' + value)

# 获得该页面所有的 local storage 的值
# 由于只有一个键值对数据，仍返回一个值，但是是list类型
# scriptArray = """return Array.apply(0, new Array(localStorage.length)).map(function (o, i)
#                 { return localStorage.getItem(localStorage.key(i)); }
# 				)"""
#
# result = driver.execute_script(scriptArray)
# print("Lets see the list of local storage - 1st:")
# print(result)
#
# # 通过 js 设置 local storage 中的值
# driver.execute_script("localStorage.setItem('Test-key','Test-value')")
#
# # 再次获取 local storage
# result = driver.execute_script(scriptArray)
# print("Lets see the list of local-storage - 2nd:")
# print(result)

# 关闭页面
# driver.close()
#
# # 创建新的 webdriver 对象，打开页面
# driver = webdriver.Firefox()
# driver.get('http://html5demos.com/storage-events')
#
# # 获取 local storage 的值
# # 与
# result = driver.execute_script(scriptArray)
# print("Lets see the list of local-storage - 3rd:")
# print(result)
#
# driver.quit()