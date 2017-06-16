__author__ = 'applewu'

# -*- encoding:utf8 -*-
from selenium import webdriver

# 这里采用了 Headless 浏览器，脚本运行过程中不会有打开浏览器页面的直观效果
# 读者可以根据自己的喜好，更换为其他类型的 driver
driver = webdriver.PhantomJS(executable_path=' /phantomjs-2.1.1-macosx/bin/phantomjs')

# demo.html 作为 iframe.html 的子页面，若要操作 demo.html 中的页面元素，
# 需要先访问 iframe.html，再切换到 demo.html 中
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Iframe/iframe.html')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

# 名称为 sub 的文本框是在 demo.html 中的，此时可以直接访问元素，输入文本
driver.find_element_by_name('sub').send_keys('1st Input')

# 名称为 parent 的文本框是在 iframe.html 中的，切换之后就可以访问元素，输入文本
driver.switch_to.default_content()
driver.find_element_by_name('parent').send_keys('2nd Input')

# 窗口最大化，新建截图文件并保存到脚本所在目录的 iframe_Ex.png
driver.maximize_window()
driver.save_screenshot('iframe_Ex.png')
driver.quit()
