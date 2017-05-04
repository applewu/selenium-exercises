# -*- coding: utf-8 -*-
__author__ = 'applewu'

from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType

desired_caps = dict()
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'Settings'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = 'Google Galaxy Nexus'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
"""
获得当前设备网络连接状态
NO_CONNECTION = 0
AIRPLANE_MODE = 1
WIFI_ONLY = 2
DATA_ONLY = 4
ALL_NETWORK_ON = 6
"""
print("The current network connection type is " + str(driver.network_connection))
driver.set_network_connection(ConnectionType.NO_CONNECTION)
print("The current network connection type is " + str(driver.network_connection))

driver.quit()