import flet as ft, random, time
from bs4 import BeautifulSoup
import re
from pyrae import dle
from pydex import dex
#from pydexen import dexen
from definitii import definitie_es as dfn_es
from definitii import definitie_ro as dfn_ro
count=10
vieti = 10
lista_caractere_ro = ['A','Ă','Â','B','C','D','E','F','G','H','I','Î','J','K','L','M','N','O','P','Q','R','S','Ș','T','Ț','U','V','W','X','Y','Z']
lista_caractere_es = ['A','B','C','D','E','F','G','H','I','J','K','L','M','Ñ','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def schimba_limba(cod_limba):

    ro=['Limbă','Ajutor','Despre','Alege limba','Română 🇷🇴','Spaniolă 🇪🇸','Litera este la poziția corectă','Litera este la poziția incorectă','Toate literele identice din cuvânt\n\t\t\t\t\t\t\t\t\t\t\t\t descoperite','Litera nu este în cuvânt','Există',
        'cuvinte din','litere','Glisează pentru a alege mărimea cuvântului','Nu, nu, nu!!! ','\t\t\t Îmi pare rău, nu ai reușit\n','\t\t\t\t\t\t  să ghicești cuvântul','\t\t\t\t\t\t\t Cuvântul era:\n','\t\t Ai reușit în \n \t','minut','secunde\n\t\t\t\t\t\t si',
        'minute','încercări ','Felicitări','Verifică','Printre cuvinte în','Limbă cuvânt','Engleză 🇬🇧']

    es=['Idioma','Ayuda','Acerca de','Elige tu idioma','Rumano 🇷🇴','Español 🇪🇸','Letra en la posición correcta','Letra en la posición incorrecta','Todas las letras iguales de la\n\t\t\t\t\t\t\t\t\t\t\t  palabra encontradas','La letra no esta en la palabra','Hay',
        'palabras de','letras','Desliza para elegir el tamaño de la palabra','No, no, no!!! ','\t\tLo siento, no has logrado\n','\t\t\t\t\t\t  encontrar la palabra','\t\t\t\t\tLa palabra era:\n','\t\t Lo has conseguido en  \n \t','minuto','segundos\n\t\t\t\t\t\t y',
        'minutos', 'intentos','Felicidades','Comprueba','Entre palabras en','Idioma palabra','Inglés 🇬🇧']
    if cod_limba == 'ro':
        lang=ro
       
    elif cod_limba=='es':
        lang=es
        
    return lang
#creamos la clase Code_show que se encarga de imprimir en pantalla los numeros necesarios de elementos para encontrar la palabra
class Code_show():
    def __init__(self,lista_caractere,choice,lang, hf):
         
         self.choice = choice
         self.lang = lang
         self.code=''
         self.hf=hf
         self.lista_caractere=lista_caractere
         self.code_value = ft.TextField(value=self.lista_caractere[0],color='orange', border_color= 'blue',focused_border_color = 'red', max_length=1,capitalization='characters', text_align='center', height=80,border_width=5,border_radius=40,col={"xs":12/len(self.choice), "md": 12/len(self.choice), "xl":12/len(self.choice)})
    def code_minus_click(self, code_value):
        self.hf.heavy_impact()
        if self.code_value.value not in self.lista_caractere:
                self.code_value.value = self.lista_caractere[0]   
        else:        
            if self.lista_caractere.index(self.code_value.value.upper()) >0:
                self.code_value.value = self.lista_caractere[self.lista_caractere.index(self.code_value.value.upper())- 1]
            
            else:
                self.code_value.value = self.lista_caractere[len(self.lista_caractere)-1]
            self.code_value.update()
            self.code_valor()
            

    def code_plus_click(self, code_value):
        self.hf.heavy_impact()
        if self.code_value.value not in self.lista_caractere:
                self.code_value.value = self.lista_caractere[0]   
        else:   
            if self.lista_caractere.index(self.code_value.value.upper()) <len(self.lista_caractere)-1:
                self.code_value.value = self.lista_caractere[self.lista_caractere.index(self.code_value.value.upper())+ 1]
            else:
                self.code_value.value = self.lista_caractere[0]
            self.code_value.update()
            self.code_valor()
            

    def valor(self):            
        return ft.Column([
                    ft.IconButton(icon ='arrow_downward_rounded', on_click = lambda *args: self.code_plus_click(self.code_value),width=1000, style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.RED,ft.MaterialState.HOVERED: ft.colors.GREEN,},bgcolor=ft.colors.WHITE10)),
                    self.code_value,
                    ft.IconButton(icon ='arrow_upward_rounded', on_click = lambda *args: self.code_minus_click(self.code_value),width=1000,style=ft.ButtonStyle(color={ft.MaterialState.DEFAULT: ft.colors.GREEN,ft.MaterialState.HOVERED: ft.colors.RED,},bgcolor=ft.colors.WHITE10)),
                    ],alignment=ft.MainAxisAlignment.CENTER,col={"xs":12/len(self.choice), "md": 12/len(self.choice), "xl":12/len(self.choice)},)
   
    def code_valor(self):
    
        return self.code_value.value

#definimos la funcion para decodificar los archivos con las palabras


def main(page: ft.Page):
    page.title = 'Cuvinte'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = 'always'    
    page.theme_mode = ft.ThemeMode.DARK
    page.spacing=5
    theme = ft.Theme()
    theme.page_transitions.android = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.NONE
    theme.page_transitions.windows = ft.PageTransitionTheme.FADE_UPWARDS
    page.theme=theme
    page.update()
    #page.window_minimize=True
    #page.window_full_screen=True
    #page.window_bgcolor = ft.colors.TRANSPARENT
    #page.bgcolor = ft.colors.TRANSPARENT
    #page.window_title_bar_hidden = Trueself.cod_pos.update() 
    #page.window_frameless = True
    #page.window_title_bar_buttons_hidden = True
    #page.window_left = 20
    #page.window_top = 10
    #page.window_height =1640
    #page.window_width=1800
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    #el menu de la pagina
    #creamos la clase Cronometru
    
    

    def game(lb,mod,lb_cuv):
        start=time.time()
        globals()['count'] = 0
        page.splash = ft.Row([ft.Text(f'',color=ft.colors.ORANGE,size=20,text_align='center')])
        lang=schimba_limba(lb)
        if lb_cuv =='es':
            lista_caractere = lista_caractere_es
        else :
            lista_caractere=lista_caractere_ro
        start_time = None
        start_time = time.time()
        x=mod.split('t')  
        globals()['vieti']=10 +int(x[1])
        def alege_cuvantul(litere,lb_cuv):
                  
            with open(f'./cuvinte/{lb_cuv}_cuvinte{litere}.cfg', 'r') as fisier_cuvinte:
                lista_cuvinte = fisier_cuvinte.readline().split(',')
            index_selectat = random.randint(0,len(lista_cuvinte)-1)
            choice = lista_cuvinte.pop(index_selectat).upper()           
            print(choice)
            return(choice)        
            
        choice = alege_cuvantul(x[1],lb_cuv)
        
        if lb_cuv=='es':
            dfn = dfn_es.definitie_es(choice)
            if dfn=='...':
              dfn= dle.search_by_word(word =choice)
            definitie = dfn
            
        elif lb_cuv=='en':
            
            definitie = '' #dexen.search_by_word(word=choice)
            #definitie.to_dict()
            
        elif lb_cuv == 'ro':
            definitie = dfn_ro.definitie_ro(choice)
            if definitie == '...':
                xc='s. |v. |adj. |; | - |interj. |vb. '
                defn= dex.search_by_word(word =choice)
                de=re.split("\"",str(defn))
                try:
                  defi =  re.split(xc,de[1],1)                
                  definitie = defi[1]
                except: 
                  try: 
                    defi =  re.split(xc,de[0],1)                
                    definitie= defi[1]
                  except: definitie = '...'
        else: definitie =''    
        page.clean()
        page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12,),       
            
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PASSWORD),
                label=lang[0],
                selected_icon=ft.icons.PASSWORD_OUTLINED,
                
            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.PASSWORD),
                label=lang[26],
                selected_icon=ft.icons.PASSWORD_OUTLINED,
                
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.HELP),
                label=lang[1],
                selected_icon=ft.icons.HELP_OUTLINE_OUTLINED,

            ),
            ft.NavigationDrawerDestination(
                icon_content=ft.Icon(ft.icons.CLOUD),
                label=lang[2],
                selected_icon=ft.icons.CLOUD_OUTLINED,

            ),
            #ft.Divider(thickness=4),
            #ft.NavigationDrawerDestination(
                #icon_content=ft.Icon(ft.icons.EXIT_TO_APP),
                #label='Exit',
                #selected_icon=ft.icons.EXIT_TO_APP_OUTLINED,

            #),
        ],on_change=lambda e:draw(e.control.selected_index),
    )

    
        def draw(selected_dest):
            
            if selected_dest == 0:
                page.drawer.open = False
                def close_dlg(*args):                
                    page.drawer.open = False
                    dlg_modal.open = False
                    hf.heavy_impact() 
                    page.drawer.update()                
                    page.update()
                def set_limba(lb):
                    page.drawer.open = False
                    dlg_modal.open = False
                    hf.heavy_impact() 
                    page.drawer.update()                
                    #page.update()
                    page.clean()
                    time.sleep(0.1)
                    game(lb,mod,lb)
                dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text(lang[3], text_align='center',size=30),
                #content=ft.Text(spans = [ft.TextSpan('Alege limba\n', ft.TextStyle(color=ft.colors.RED, size=18, weight=ft.FontWeight.BOLD,))]),
                actions=[ft.TextButton(lang[4], on_click=lambda e: set_limba('ro')),ft.TextButton(lang[5], on_click=lambda e: set_limba('es')), ],actions_alignment=ft.MainAxisAlignment.CENTER,
                    )
                hf.heavy_impact()         
                page.dialog = dlg_modal
                dlg_modal.open = True           
                page.update()
            elif selected_dest == 1:
                page.drawer.open = False
                def close_dlg(*args):                
                    page.drawer.open = False
                    dlg_modal.open = False
                    hf.heavy_impact() 
                    page.drawer.update()                
                    page.update()
                def set_limba_cuv(lb_cuv):
                    hf.heavy_impact()                    
                    page.drawer.open = False
                    dlg_modal.open = False
                    page.drawer.update()                
                    #page.update()
                    page.clean()
                    time.sleep(0.1)
                    game(lb,mod,lb_cuv)
                dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text(lang[26], text_align='center',size=30),
                #content=ft.Text(spans = [ft.TextSpan('Alege limba\n', ft.TextStyle(color=ft.colors.RED, size=18, weight=ft.FontWeight.BOLD,))]),
                actions=[ft.TextButton(lang[4], on_click=lambda e: set_limba_cuv('ro')),ft.TextButton(lang[5], on_click=lambda e: set_limba_cuv('es')),ft.TextButton(lang[27], on_click=lambda e: set_limba_cuv('en')), ],actions_alignment=ft.MainAxisAlignment.CENTER,
                    )
                hf.heavy_impact()        
                page.dialog = dlg_modal
                dlg_modal.open = True           
                page.update()

            elif selected_dest == 2:
                def close_dlg(*args):                
                    page.drawer.open = False
                    dlg_modal.open = False
                    hf.heavy_impact()
                    page.drawer.update()                
                    page.update()
                dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text(lang[1], text_align='center',size=30),
                content=ft.Text(
                    spans=[
                        ft.TextSpan(f'oo',ft.TextStyle(bgcolor=ft.colors.GREEN,color=ft.colors.GREEN, weight=ft.FontWeight.BOLD,)),
                        ft.TextSpan(f'\t{lang[6]}\n'),
                        ft.TextSpan(f'oo',ft.TextStyle(bgcolor=ft.colors.ORANGE,color=ft.colors.ORANGE, weight=ft.FontWeight.BOLD,)),
                        ft.TextSpan(f'\t{lang[7]}\n'),
                        ft.TextSpan(f'oo',ft.TextStyle(bgcolor=ft.colors.RED,color=ft.colors.RED, weight=ft.FontWeight.BOLD,)),
                        ft.TextSpan(f'\t{lang[9]}\n'),
                        ft.TextSpan(f'oo',ft.TextStyle(bgcolor=ft.colors.BLUE,color=ft.colors.BLUE, weight=ft.FontWeight.BOLD,)),
                        ft.TextSpan(f'\t{lang[8]}'),
                                          
                    ]),
                    actions=[ft.TextButton('Ok', on_click=close_dlg),], actions_alignment=ft.MainAxisAlignment.CENTER,
                    )
                        
                page.dialog = dlg_modal
                hf.heavy_impact()
                dlg_modal.open = True           
                page.update()

            elif selected_dest ==3:
                def close_dlg(*args):
                    dlg_modal.open = False
                    page.drawer.open = False
                    time.sleep(0.1)                  
                    page.drawer.update()
                    hf.heavy_impact()
                    page.update()
                dlg_modal = ft.AlertDialog(
                modal=True,
                title=ft.Text(lang[2], text_align='center',size=24),
                content=ft.Text(f' Made with ❤️ by Alexandru G. Muntenas \n \t\t\t\tfor my son and my wife ', size=14, text_align='center'),
                actions=[ft.TextButton('Ok', on_click=close_dlg),], actions_alignment=ft.MainAxisAlignment.END,
                    )
                
            
                page.dialog = dlg_modal
                hf.heavy_impact()
                dlg_modal.open = True
                page.update()

            elif selected_dest == 4:
                page.window_close()

        def show_drawer(e):
            time.sleep(0.1)
            hf.heavy_impact()
            page.drawer.open = True
            #page.drawer.update()
            
        if lb =='ro' and lb_cuv == 'ro':idl='Română 🇷🇴'
        elif lb =='ro' and lb_cuv == 'es':idl='Spaniolă 🇪🇸'
        elif lb =='ro' and lb_cuv == 'en':idl='Engleză 🇬🇧'
        elif lb =='es' and lb_cuv == 'ro':idl='Rumano 🇷🇴'            
        elif lb =='es' and lb_cuv == 'es':idl='Español 🇪🇸'
        elif lb =='es' and lb_cuv == 'en':idl='Inglés 🇬🇧'
        #page.appbar = ft.CupertinoAppBar(leading = ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.BLUE, on_click=show_drawer),bgcolor=ft.colors.SURFACE_VARIANT,middle=ft.Text(f'{lang[25]} {idl}'))
        
        

        page.appbar = ft.AppBar(title=ft.Text(f'{lang[25]} {idl}'),center_title=True,bgcolor=ft.colors.SURFACE_VARIANT)

        
        
        #slide buttton
        def handle_change(e):
            
            slider_value.value = f'{lang[11].capitalize()} {int(e.control.value)+3} {lang[12]}'
            hf.heavy_impact()
            x = slider_value.value.split(' ')
            page.update()
            time.sleep(1)
            #print(x[2])
            nr = x[2]
            mod = f'cuvant{x[2]}'            
            page.update()
            game(lb,mod,lb_cuv)

        
        (slider_value := ft.Text(f"{lang[11].capitalize()} {x[1]} {lang[12]}",color=ft.colors.ORANGE,size=20,text_align='center'))
        page.navigation_bar  = ft.Row([ft.CupertinoSlider(divisions=9,max=9,active_color=ft.colors.RED,thumb_color=ft.colors.GREEN,value = int(x[1])-3 ,scale = 1.3,on_change=handle_change,tooltip=lang[13]),ft.Row([ft.Text('    ')]),],alignment=ft.MainAxisAlignment.END)
    
       
        page.add(ft.Row([slider_value,ft.Text(' ')],alignment=ft.MainAxisAlignment.END,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},),                 )
        #print(len(choice)).
        with open('./rock.cfg','w') as cfg:
            conf = f'{lb},{mod},{lb_cuv}'
            cfg.writelines(conf)
        def verifica(code):
            '''Verificam codul introdus '''
          
            def check (choice ,code,pos): 
                if code[pos] not in lista_caractere:
                    checked = ft.TextField(value=lang[12].capitalize(), text_align='center',height=60,border_width=5,border_radius=40,border_color='white',tooltip=lang[12],read_only=True,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},)
                       
                elif code[pos]==choice[pos]:
                    checked = ft.TextField(value=code[pos], text_align='center',height=60,border_width=5,border_radius=40,border_color='green',tooltip=lang[6],read_only=True,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},)
                elif code[pos] in choice and code.count(code[pos]) > choice.count(code[pos]): #and (code[0] != y and code[0] != z and code[0] != w and code[0] != q):
                    checked= ft.TextField(value=code[pos], text_align='center',height=60,border_width=5,border_radius=40,border_color='blue',tooltip=lang[8],read_only=True,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},) 
                elif code[pos] in choice :
                    checked = ft.TextField(value=code[pos], text_align='center', height=60,border_width=5,border_radius=40,border_color='orange',tooltip=lang[7],read_only=True,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},) 
                else:
                    checked = ft.TextField(value=code[pos], text_align='center',height=60,border_width=5,border_radius=40,border_color='red',tooltip=lang[9],read_only=True,col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},)
                return checked 
            res = []
            fel=0
            for i in range(len(choice)):
                res.append(check(choice,code,i))
                if code[i]==choice[i]:
                    fel+=1           
            
            if fel == len(choice):
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                open_dlg_modal(start_time)
            else: 
                pass
                            
            
            return res  
        
            
            
        def increment():
            globals()['count'] += 1 
            globals()['vieti'] -= 1
            page.splash = ft.Row([ft.Text(f'{lang[22].capitalize()}: {count}',color=ft.colors.ORANGE,size=20,text_align='center')])
        def code_check(*args):
            hf.heavy_impact()
            hf.heavy_impact()
            code=''
            for i in lista:
                code+=i.code_valor()
                           
            #print(code)
         
            increment()
            if vieti == 0:
                def close_dlg(*args):  
                    dlg.open = False 
                    page.drawer.open = False
                    page.update()
                    hf.heavy_impact()
                    time.sleep(0.1)
                    globals()['count'] = 0
                    game(lb,mod,lb_cuv)                                                   
                dlg = ft.AlertDialog(modal =True,title=ft.Text(lang[14], text_align='center',size=30),
                    content=ft.Text(f'{lang[15]} {lang[16]}.\n{lang[17]} {choice}\n {definitie}', text_align='center'),actions=[ft.TextButton('Ok', on_click=close_dlg)],actions_alignment=ft.MainAxisAlignment.END,
                    on_dismiss= close_dlg)
                page.dialog=dlg 
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                dlg.open = True
                page.update()       
                
                            
            animsw=[]
            for x in verifica(code.upper()):
                animsw.append(ft.AnimatedSwitcher(x,))
            pozitii =[]
            check_vals=[]
            for i in verifica(code.upper()):
                sw=ft.AnimatedSwitcher(i,)
                check_vals.append(i)
                pozitii.append(sw)
                        
            for i in range(len(choice)):                
                lista_container[i].content = pozitii[i]                
            page.update()    
                
                
            for i in range(len(choice)):                
                lista_cont_probe[i].content.controls.insert(0,check_vals[i])
                lista_container[i].update()
        
        
           
        
            
        def open_dlg_modal(*args):
            def close_dlg(*args):
                dlg_modal.open = False
                page.update()
                hf.heavy_impact()
                globals()['count'] = 0
            stop=time.time()
            durata = stop-start
            minute = durata//60
            secunde = durata - minute*60
            

                       
            msg =ft.Text(f'{lang[18]} {count} {lang[22]}.\n{lang[17]} {choice}\n ⌛ {minute:.0f}:{secunde:.0f}', text_align='center')
            
            dlg_modal = ft.AlertDialog(modal=True,title=ft.Text(lang[23], text_align='center',size=30),content=msg,
                actions=[ft.TextButton('Ok', on_click=close_dlg),],
                actions_alignment=ft.MainAxisAlignment.END,
                on_dismiss=lambda e: game(lb,mod,lb_cuv),)
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
    
        # CONTAINERE REZULTATE
        
        lista=[Code_show(lista_caractere,choice,lang, hf) for i in range(len(choice))]
        lista_container=[ft.Container(col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},) for i in range(len(choice))]
        lista_cont_probe = [ft.Container(col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)}, height=143) for i in range(len(choice))]#243
        for i in range(len(choice)):  
                lista_cont_probe[i].content = ft.ListView(spacing=1)
                lista_cont_probe[i].scroll = 'always'    
        
             
        #page.show_snack_bar(ft.SnackBar(content=ft.Text(definitie)))
        page.add(      
            ft.ResponsiveRow([ft.Text(definitie)],alignment=ft.MainAxisAlignment.CENTER),     
            ft.ResponsiveRow([i.valor() for i in lista],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([ft.ElevatedButton(lang[24],color='blue', icon='check', icon_color='orange',scale=1.5,on_click=code_check)],alignment=ft.MainAxisAlignment.CENTER,col={"xs": 12/len(choice), "md": 12/len(choice)}), 
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),      
            ft.ResponsiveRow([i for i in lista_container],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([i for i in lista_cont_probe],alignment=ft.MainAxisAlignment.CENTER),           
                    
        )
    '''try:
        with open('./rock.cfg','r') as cfg:
            cfg = cfg.readline().split(',')
            print(cfg)
            lb = cfg[0]
            mod= cfg[1]
            lb_cuv = cfg[2]
        game(lb,mod,lb_cuv)    
    except: game('ro','cuvant6','ro')'''
  
    game('ro', 'cuvant5', 'ro')
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER) #view=ft.AppView.WEB_BROWSER, 
