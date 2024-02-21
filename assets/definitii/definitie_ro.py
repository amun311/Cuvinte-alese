import re
#import requests
import urllib.request as urllib
#import urllib.request
#from urllib.parse import urljoin
from bs4 import BeautifulSoup
def definitie_ro(cuv):
    '''user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }'''
    try:
      url = f'https://m.dex.ro/?word={cuv}'
      #url  =urljoin('https://dex.ro','//dex.ro/{}'.format(cuv))
      req = urllib.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0'}, origin_req_host=None, unverifiable=False, method=None)
      response = urllib.urlopen(req)
      #response =requests.get(url)
      page = response.read()
      page = response.content
      soup = BeautifulSoup(page.decode(), 'html.parser')
      '''req = urllib.Request(f'https://dex.ro/{cuv}', None, headers)
      response = urllib.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')'''
      #print(soup)
      response.close() 
    except: soup = ''
    #pt1 = r'</i> \d\) ((\w*\s*,?)*.) '
    pt1 = r'</i>\)? \d\)?.? ?((\w*\s*,?)*.) '
    pt2 = r'</span>((\w*\s*,*\(?\)?)*.) '
    pt3 = r'<meta content=\"\w+,? ?-?\w+,? ?\w+?,? ? -?(\w*\s*,? ?-?.*)◊?\" '
    pt4 =r'</strong> ((\w*\s*,*;?)*.)'
    definitie='...'
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

    return definitie

