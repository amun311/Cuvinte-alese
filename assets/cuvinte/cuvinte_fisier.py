list_cuv=[]
z=[]
with open('/home/alexandru/Development/Projects/flet/cuvinte/text.txt','r') as f:
    x = f.readlines()
    for cuv in x:
        cuv=cuv.split()
        z.append(cuv[0])

print(z)
  
mal = ['list','script','fdex']
for i in range(3,4):
    lac = []
    for cuv in z:        
        if len(cuv) == i and cuv not in lac and cuv not in mal and "'" not in cuv:
            lac.append(cuv)
                
            with open(f'/home/alexandru/Development/Projects/flet/cuvinte/ro_cuvinte{i}.cfg','w') as f:
                for cuv in lac:
                    f.writelines(cuv+',')
