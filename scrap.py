from selenium import webdriver
import re
from xlrd import open_workbook
from xlutils.copy import copy
driver = webdriver.Chrome()
file_name='E:\\saledata.xls'
rb=open_workbook(file_name)
wb=copy(rb)
rsheet=rb.sheet_by_index(0)
wsheet=wb.get_sheet(0)
for i in range(rsheet.nrows):
    offers=[]
    url=rsheet.cell(i,0).value
    #wsheet.write(i,1,'fetched')
    driver.get(url)
    sel_source=driver.page_source
    x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)", sel_source,re.IGNORECASE)
    disct=set(x)
    li=[]
    for i in disct:
        li.append(''.join(i))
    s=', '.join(str(e) for e in li)
    wsheet.write(i,1,s)
    print s
    #print disct
    #for i in disct:
	#offers.append("".join(i))
	#wsheet.write(i,1,disct)    
driver.close()
wb.save(file_name)

