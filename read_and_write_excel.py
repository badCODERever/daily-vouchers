from xlrd import open_workbook
from xlutils.copy import copy
rb=open_workbook('E:\\sample.xls')
wb=copy(rb)
rsheet=rb.sheet_by_index(0)
wsheet=wb.get_sheet(0)
for i in range(rsheet.nrows):
    print rsheet.cell(i,0).value
    wsheet.write(i,1,'fetched')
wb.save('E:\\sample.xls')
    
