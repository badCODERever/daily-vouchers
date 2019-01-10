import requests
import re
from bs4 import BeautifulSoup
url = 'http://localhost:88/documentation.html'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
for string in soup.stripped_strings:
    print repr(string)

