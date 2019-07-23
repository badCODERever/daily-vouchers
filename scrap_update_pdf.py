import pytesseract
from PIL import Image
from pytesseract import image_to_string
from selenium import webdriver
import re
from xlrd import open_workbook
from xlutils.copy import copy


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'

driver = webdriver.Chrome()
file_name='E:\activerstorelist - Copy (2).xls'
rb=open_workbook(file_name,'wb')#open file with writemode
wb=copy(rb)
rsheet=rb.sheet_by_index(0)
wsheet=wb.get_sheet(0)
for i in range(1,rsheet.nrows):
    url=rsheet.cell(i,0).value
    driver.get(url)
    sel_source=driver.page_source
    driver.save_screenshot('screen.png')
    myText = image_to_string(Image.open('screen.png')).lower()
    print(myText)
driver.close()



