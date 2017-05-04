__author__ = 'applewu'

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://www.pingxx.com/')
value = driver.execute_script("return sessionStorage.getItem(sessionStorage.key(0));")
print 'The first value is ' + value

scriptArray = """return Array.apply(0, new Array(sessionStorage.length)).map(function (o, i)
                { return sessionStorage.getItem(sessionStorage.key(i)); }
				)"""

result = driver.execute_script(scriptArray)
print result

driver.execute_script("sessionStorage.clear();")

driver.close()