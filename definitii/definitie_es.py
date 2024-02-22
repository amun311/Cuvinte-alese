import re
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
def definitie_es(cuv):
    user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }
    try:
      url  =urljoin('https://dle.rae.es','//dle.rae.es/{}'.format(cuv))
      req = urllib.request.Request(url, None, headers)
      response = urllib.request.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')
      '''req = urllib.Request(urlparse.quote(f'https://dle.rae.es/{cuv}'), None, headers)
      response = urllib.urlopen(req)
      page = response.read()
      soup = BeautifulSoup(page.decode(), 'html.parser')'''
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