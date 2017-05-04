# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://cdn.sencha.com/touch/sencha-touch-2.4.1/examples/video/index.html')

# 单击页面，以显示视频对象
div_background = driver.find_element_by_id('ext-element-7')
div_background.click()

# 获得视频地址和时长
video_element = driver.find_element_by_id('ext-element-8')
source = driver.execute_script("return arguments[0].currentSrc;", video_element)
print("The path of video is " + source)
duration = driver.execute_script("return arguments[0].duration;", video_element)
print("The duration of video is {0} seconds".format(str(duration)))

# 控制视频的暂停和播放
time.sleep(10)
driver.execute_script("return arguments[0].pause();", video_element)
time.sleep(5)
driver.execute_script("return arguments[0].play();", video_element)

driver.close()