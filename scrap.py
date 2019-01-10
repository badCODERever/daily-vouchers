from selenium import webdriver
import re
driver = webdriver.Chrome()
driver.get('https://www.farfetch.com/in/')
sel_source=driver.page_source
x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)", sel_source,re.IGNORECASE)
disct=set(x)
for i in disct:
	print "".join(i)
driver.close()


