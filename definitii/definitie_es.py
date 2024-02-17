import re
import urllib.request as urllib
from bs4 import BeautifulSoup
def definitie_es(cuv):
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    try:
      req = urllib.Request(f'https://dle.rae.es/{cuv}', None, headers)
      response = urllib.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')
      #print(soup)
      response.close() 
    except: soup = ''
    pt = r'1. (\w{1,}. \w*\s*.*).\",'
    definitie = re.search(pt,str(soup))
    #definitie = str(definitie)
    try:
        definitie= definitie.group(1)
    except:
        definitie = ''
    dfn = str(definitie).lstrip("['").rstrip("']")
    
    return dfn
'''print(definitie_es('vagina'))
print(definitie_es('caballo'))
print(definitie_es('hombre'))'''
'''from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
import re
def definitie_es(cuv):
    pt1 =r'<li>(?!\w{2}\.)(\w*\s*.*)<br/></li></o'
    
    
    pt2 = r'</span>(\w*\s*.*,*):<br/>'
    
    pt3 = r'\"i\">(\w*\s*.*,*)</span> '
    pt4 = r"ol class=\"entry\"><li>(\w*\s*.*,*)<li>"
    url = f'https://www.wordreference.com/definicion/{cuv}'
    response = requests.get(url)   
    html_content = response.content
    xc='span>'
    #print(html_content.decode())
    soup = BeautifulSoup(html_content.decode(), 'html.parser')
    meta = soup.find_all('ol', attrs={'class':'entry'})
    #print(meta)
    def definitie(pt):
        if len(meta)==1:
            defin= re.findall(pt,str(meta[0]))
            
        elif len(meta)>1:
            defin0= re.findall(pt,str(meta[0]))
            defin1= re.findall(pt,str(meta[1]))

            if len(str(defin0)) > len(str(defin1)):
                defin= defin0
               
            else:
                defin= defin1
            
        else:
            defin = 'No encuentro definicion' 
        
        return defin
    
    
    defin1 = definitie(pt1)
    defin2 = definitie(pt2)
    defin3 = definitie(pt3)
    defin4 = definitie(pt4)  
    
    #print('defin1: ',len(str(defin1)), ' defin2: ',len(str(defin2))+30, ' defin3: ',len(str(defin3)), ' defin4: ',len(str(defin4))) 
    #print('defin1: ',defin1, ' defin2: ',defin2,' defin3: ',defin3,' defin4: ',defin4)
    if len(str(defin1))>len(str(defin3)) and len(str(defin1))>len(str(defin2))+30 and len(str(defin1))>len(str(defin4)):
        defin = defin1
    elif  len(str(defin2))+30>len(str(defin1)) and len(str(defin2))+30>len(str(defin3)) and len(str(defin2))+30>len(str(defin4)):
        defin = defin2   
    elif len(str(defin3))>len(str(defin1)) and len(str(defin3))>len(str(defin2))+30 and len(str(defin3))>len(str(defin4)):
        defin = defin3
    elif len(str(defin4))>len(str(defin1)) and len(str(defin4))>len(str(defin2))+30 and len(str(defin4))>len(str(defin3)):
        defin = defin4
    else: defin = defin1
    x=re.split("<li>|<br|span>",str(defin))
    
    #print(defin)    
    
    try:
        y = re.split(xc,x[0],1)
        definit = y[1]
    except:definit=(x[0].lstrip("['").rstrip(':\']'))
    return definit
""""""
print('Definitia este: ',definitie_es('halamos'))
print('Definitia este: ',definitie_es('nanay'))
print('Definitia este: ',definitie_es('caca'))'''