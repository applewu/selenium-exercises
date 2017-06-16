# -*- coding: utf-8 -*-
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('file:///Users/applewu/Documents/iCode/selenium/ch03/Table/table.html')

# 这里Javascript 的用意是，根据元素标签 td 获得单元格元素集合，
# 再找到“康乃馨”单元格，最后点击它所在行的 CheckBox 元素
jscript = '''var cells = document.getElementsByTagName("td");
for(var x = 0; x < cells.length; x++)
{{if(cells[x].innerHTML == '{0}')
{{cells[x].parentNode.childNodes[1].childNodes[1].click();
break;
}}}}'''.format('康乃馨')

# 执行完下面语句之后，将看到页面上的 CheckBox 元素被选中了
driver.execute_script(jscript)