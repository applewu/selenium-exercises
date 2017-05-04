# -*- coding: utf-8 -*-
__author__ = 'applewu'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# driver = webdriver.Firefox()
# driver.get('http://galacticmilk.com/sketchpad/')
# ApplicationCache = driver.application_cache
# print(ApplicationCache.status)
# driver.close()

desired_caps = dict()
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = 'Settings'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.0'
desired_caps['deviceName'] = 'Google Galaxy Nexus'

driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', desired_caps)
# driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', DesiredCapabilities.ANDROID)

print("The current network connection type is " + driver.mobile.network_connection)
