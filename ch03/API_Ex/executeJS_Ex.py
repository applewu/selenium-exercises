__author__ = 'applewu'

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://cn.bing.com/")

# Check if the jquery existed
result_1 = driver.execute_script("return typeof jQuery!= 'undefined';")
assert result_1 is False

jq_script = "https://code.jquery.com/jquery-1.9.1.min.js"
driver.execute_script("function inject_script(url) {"
                      "var script = document.createElement('script');"
                      "script.src = url;"
                      "var head = document.getElementsByTagName('head')[0];"
                      "head.appendChild(script);}"
                      "inject_script(arguments[0]);", jq_script)

# Check if the jquery existed again
result_2 = driver.execute_script("return typeof jQuery!= 'undefined';")
assert result_2 is True

# driver.quit()