# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Table/table.html')
jscript = '''var cells = document.getElementsByTagName("td");
for(var x = 0; x < cells.length; x++)
{{if(cells[x].innerHTML == '{0}')
{{cells[x].parentNode.childNodes[1].childNodes[1].click();
break;
}}}}'''.format('康乃馨')
driver.execute_script(jscript)