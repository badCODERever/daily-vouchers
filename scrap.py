from selenium import webdriver
import re
from xlrd import open_workbook
from xlutils.copy import copy
driver = webdriver.Chrome()
file_name='E:\\saledata.xls'
rb=open_workbook(file_name,'wb')
wb=copy(rb)
rsheet=rb.sheet_by_index(0)
wsheet=wb.get_sheet(0)
for i in range(rsheet.nrows):  
    url=rsheet.cell(i,0).value
    driver.get(url)
    sel_source=driver.page_source
    x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)", sel_source,re.IGNORECASE)
    disct=set(x)
    li=[]
    for j in disct:
        li.append(''.join(j))
    s=', '.join(str(e) for e in li)
    wsheet.write(i,1,s)
    wb.save(file_name)
driver.close()


