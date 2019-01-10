Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> txt='''This is the information that we have Up to 50% Off on our site for footwear, and Extra 10% Off for a new customers by use CODE: NEW10. There is a offer on Bag 25% Off. Offer and Sales based on availability of stock use vouchers to get price detection.'''
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)", txt)

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    x = re.findall("(Up to \d\d% Off)|(\d\d% Off)", txt)
NameError: name 're' is not defined
>>> import re
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)", txt)
>>> x
[('Up to 50% Off', ''), ('', '10% Off'), ('', '25% Off')]
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)", txt)
>>> x
[('Up to 50% Off', '', ''), ('', '', 'Extra 10% Off'), ('', '25% Off', '')]
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)|(Offer)", txt)
>>> x
[('Up to 50% Off', '', '', ''), ('', '', 'Extra 10% Off', ''), ('', '25% Off', '', ''), ('', '', '', 'Offer')]
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)|(Offer)|(Sale)|(Voucher)", txt)
>>> x
[('Up to 50% Off', '', '', '', '', ''), ('', '', 'Extra 10% Off', '', '', ''), ('', '25% Off', '', '', '', ''), ('', '', '', 'Offer', '', ''), ('', '', '', '', 'Sale', '')]
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)|(Offer)|(Sale)|(voucher)", txt)
>>> x
[('Up to 50% Off', '', '', '', '', ''), ('', '', 'Extra 10% Off', '', '', ''), ('', '25% Off', '', '', '', ''), ('', '', '', 'Offer', '', ''), ('', '', '', '', 'Sale', ''), ('', '', '', '', '', 'voucher')]
>>> type(x)
<type 'list'>
>>> for i in x:
	print i

	
('Up to 50% Off', '', '', '', '', '')
('', '', 'Extra 10% Off', '', '', '')
('', '25% Off', '', '', '', '')
('', '', '', 'Offer', '', '')
('', '', '', '', 'Sale', '')
('', '', '', '', '', 'voucher')
>>> for i in x:
	print i.trim

	

Traceback (most recent call last):
  File "<pyshell#20>", line 2, in <module>
    print i.trim
AttributeError: 'tuple' object has no attribute 'trim'
>>> for i in x:
	print "".join(i)

	
Up to 50% Off
Extra 10% Off
25% Off
Offer
Sale
voucher
>>> from selenium import webdriver
>>> driver.webdriver.Chrome()

Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    driver.webdriver.Chrome()
NameError: name 'driver' is not defined
>>> driver=webdriver.Chrome()
>>> driver.get('https://www.weirdfish.co.uk/')
>>> page=driver.page_source
>>> x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)|(Offer)|(Sale)|(voucher)", page)
>>> x
[(u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'70% Off', u'', u'', u'', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'Sale', u''), (u'', u'', u'', u'', u'', u'voucher'), (u'', u'', u'', u'', u'', u'voucher')]
>>> for i in x:
	print "".join(i)

	
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
Sale
70% Off
Sale
Sale
voucher
voucher
>>> disct=set
>>> disct=set(x)
>>> dict
<type 'dict'>
>>> disct
set([(u'', u'', u'', u'', u'', u'voucher'), (u'', u'70% Off', u'', u'', u'', u''), (u'', u'', u'', u'', u'Sale', u'')])
>>> for i in disct:
	print "".join(i)

	
voucher
70% Off
Sale
>>> 
