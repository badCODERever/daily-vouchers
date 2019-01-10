Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from os.path import join
>>> from xlrd import open_workbook
>>> rb=open_workbook(join('E:\\saledata.xls'),formatting_info=True,on_demand=True)
>>> rb.sheet_by_index(0).cell(0,0).value
u'https://www.allsaints.com/'
>>> rb.nrows

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    rb.nrows
AttributeError: 'Book' object has no attribute 'nrows'
>>> sheet=rb.sheet_by_index(0)
>>> sheet.nrows
11
>>> 
>>> for i in range(sheet.nrows):
	sheet.cell(i,0).value

	
u'https://www.allsaints.com/'
u'http://www.asos.com/women/'
u'https://www.aspinaloflondon.com/'
u'https://www.aureliaskincare.com/'
u'http://www.boden.co.uk/'
u'https://chescadirect.co.uk/'
u'https://www.clarks.co.uk/'
u'http://world.coach.com/'
u'https://www.coggles.com/'
u'http://www.designerdesirables.com/'
u'http://www.dorothyperkins.com/?geoip=home'
>>> from xlutils.copy imoprt copy
SyntaxError: invalid syntax
>>> from xlutils.copy import copy
>>> wb=copy(rb)
>>> wb
<xlwt.Workbook.Workbook object at 0x02BD0D50>
>>> 
