from selenium import webdriver
import re
from PIL import Image
import pytesseract
from pytesseract import image_to_string
#import cv2
#from xlrd import open_workbook
#from xlutils.copy import copy
driver = webdriver.Chrome()
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# file_name='E:\\activerstorelist.xls'
# rb=open_workbook(file_name,'wb')#open file with writemode
# wb=copy(rb)
# rsheet=rb.sheet_by_index(0)
# wsheet=wb.get_sheet(0)
# for i in range(1,rsheet.nrows):
#     url=rsheet.cell(i,0).value
driver.get("http://cbi.gov.in/rnotice/A-6889-6-2018.pdf")
sel_source=driver.page_source
driver.save_screenshot('screen.png')
im=Image.open('screen.png')
im.save('screen.png')
myText = image_to_string(Image.open('screen.png')).lower()
print(myText)
#x = re.findall("(Up to \d\d% Off)|(\d\d% Off)|(Extra \d\d% Off)", sel_source,re.IGNORECASE)
#disct=set(x)
#print(disct)
#li=[]
#for j in disct:
#    li.append(''.join(j))
#s=', '.join(str(e) for e in li)
#print (s)
    # yvalue=rsheet.cell(i,1).value
    # wsheet.write(i,2,yvalue)
    # wsheet.write(i,1,s)
    # if s==yvalue:
    #     print("No Changes in Offer")
    #     wsheet.write(i,3,"No Change")
    # else:
    #     print("Offer got changed")
    #     wsheet.write(i, 3, "Change in Offer")
    # wb.save(file_name)
#driver.close()



