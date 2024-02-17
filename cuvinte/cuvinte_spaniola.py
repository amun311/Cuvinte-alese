import requests
import re

listalt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
list_cuv=[]
for lt in listalt:
    #pt =r"\'>(\D[A-Z]*[a-z]*)</a>" 
    pt =r"\>(\D[A-ZÑ]*[a-zñ]*)\<\/"    
    url = f'https://www.palabrasque.com/buscador.php?i={lt}&f=&tv=&button=Buscar+palabras&ms=&mns=&m=&mn=&fs=0&fnl=0&fa=0&d=0'
    response = requests.get(url)   
    html_content = response.content
    words=re.findall(pt, html_content.decode())
    for cuvant in words:
        if cuvant not in list_cuv:
            list_cuv.append(cuvant)
print(list_cuv)
  
mal = ['list','script','fdex']
for i in range(3,22):
    lac = []
    for cuv in list_cuv:        
        if len(cuv) == i and cuv not in lac and cuv not in mal:
            lac.append(cuv)
                
            with open(f'/home/alexandru/Development/Projects/flet/cuvinte/es_cuvinte{i}.cfg','w') as f:
                for cuv in lac:
                    f.writelines(cuv+',')
