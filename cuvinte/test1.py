from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import re
cuv='asa'
data = []
pt =r"(=\")(\w*\s*,.*)(\d).(\w*\s*,*)*"
url = f'https://dex.ro/{cuv}'
response = requests.get(url)   
html_content = response.content
xc='s. |v. |adj. |; | - |interj.'
soup = BeautifulSoup(html_content.decode(), 'html.parser')
meta = soup.find_all('meta', attrs={'name':'description'})
print(meta)
x=re.split("\"",str(meta))
print(x[1])
y = re.split(xc,x[1],1)
print(y[1])
'''

for met in meta:
    temp_data = [met]
    for tag in meta:
        if tag.name == 'h2':
            break
        elif tag.name == 'meta':
            temp_data.append(tag)
            
    data.append(temp_data)
print(data[0][1])    
words=re.findall(pt, str(meta))
print(words)'''