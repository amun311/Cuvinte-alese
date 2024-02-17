from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import re
cuv='vagina'

pt =r"ol class=\"entry\"><li>(\w*\s*.*,*)<li>"
url = f'https://www.wordreference.com/definicion/{cuv}'
response = requests.get(url)   
html_content = response.content
xc='span>'
#print(html_content.decode())
soup = BeautifulSoup(html_content.decode(), 'html.parser')
meta = soup.find_all('ol', attrs={'class':'entry'})
print(meta)

if len(meta)==1:
    defin= re.findall(pt,str(meta[0]))
elif len(meta)>1:
    defin0= re.findall(pt,str(meta[0]))
    defin1= re.findall(pt,str(meta[1]))

    if len(defin0) > len(defin1):
        defin= defin0
        print(defin)
    else:
        defin= defin1
else:
     defin = 'No encuentro definicion'       
x=re.split("<li>|<br|span>",str(defin))
#print(defin)    
print(x[0].lstrip("['").strip(':'))
try:
    y = re.split(xc,x[0],1)
    print(y[1])
except:pass
