import re
import urllib.request as urllib
from bs4 import BeautifulSoup
def definitie_ro(cuv):
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    try:
      req = urllib.Request(f'https://dex.ro/{cuv}', None, headers)
      response = urllib.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')
      #print(soup)
      response.close() 
    except: soup =''
    #pt1 = r'</i> \d\) ((\w*\s*,?)*.) '
    pt1 = r'</i>\)? \d\)?.? ?((\w*\s*,?)*.) '
    pt2 = r'</span>((\w*\s*,*\(?\)?)*.) '
    pt3 = r'<meta content=\"\w+,? ?-?\w+,? ?\w+?,? ? -?(\w*\s*,? ?-?.*)◊?\" '
    pt4 =r'</strong> ((\w*\s*,*;?)*.)'
    definitie=''
    definitie1=''
    definitie2=''
    definitie3=''
    definitie4=''
    try:
        defn = re.search(pt1,str(soup))        
        definitie1  = defn.group(1)
    except:pass
            
    try: 
        defn = re.search(pt2,str(soup))
        definitie2  = defn.group(1)
    except:pass

    
    try: 
        defn = re.search(pt3,str(soup))
        definitie3  = defn.group(1)
    except:pass
    try: 
        defn = re.search(pt4,str(soup))
        definitie4  = defn.group(1)
    except:pass
    defn_list = [definitie1,definitie2,definitie3,definitie4]
    for defn in defn_list:
        if len(str(defn)) >= len(str(definitie)):
            definitie = defn
    '''if len(str(definitie1))>len(str(definitie3)) and len(str(definitie1))>len(str(definitie2)) and len(str(definitie1))>len(str(definitie4)):
        definitie = definitie1
    elif  len(str(definitie2))+30>len(str(definitie1)) and len(str(definitie2)) >len(str(definitie3)) and len(str(definitie2))+30>len(str(definitie4)):
        definitie = definitie2   
    elif len(str(definitie3))>len(str(definitie1)) and len(str(definitie3))>len(str(definitie2)) and len(str(definitie3))>len(str(definitie4)):
        definitie = definitie3
    elif len(str(definitie4))>len(str(definitie1)) and len(str(definitie4))>len(str(definitie2)) and len(str(definitie4))>len(str(definitie3)):
        definitie = definitie4'''
    return definitie


'''print('definitie: ',definitie_ro('cal'))
print('definitie: ',definitie_ro('autobuz'))
print('definitie: ',definitie_ro('albastru'))
print('definitie: ',definitie_ro('serpentine'))
print('definitie: ',definitie_ro('nordic'))'''
'''from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import re
def definitie_ro(cuv):
    pt =r"(=\")(\w*\s*,.*)(\d).(\w*\s*,*)*"
    url = f'https://dex.ro/{cuv}'
    response = requests.get(url)   
    html_content = response.content
    try:
        text = html_content.decode(encoding='utf-32')
    except: 
        text = html_content
    xc='s. |v. |adj. |; | - |interj. |vb. '
    soup = BeautifulSoup(text, 'html.parser')
    meta = soup.find_all('meta', attrs={'name':'description'})
    #print(meta)
    x=re.split("\"",str(meta))
    #print(x[1])
    y = re.split(xc,x[1],1)
    #print(y[1])
    try:
        res = y[1]
    except:
        res = 'Nu gasesc definitia la cuvant'
    return res

print(definitie_ro('munca'))
''''''

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