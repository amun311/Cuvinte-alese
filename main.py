import flet as ft, random, time, os
import requests
import pickle
import flet.version
color='LIGHT'
ex=0
count=10
vieti = 10
lista_caractere_ro = ['A','Ă','Â','B','C','D','E','F','G','H','I','Î','J','K','L','M','N','O','P','Q','R','S','Ș','T','Ț','U','V','W','X','Y','Z']
lista_caractere_es = ['A','Á','B','C','D','E','É','F','G','H','I','Í','J','K','L','M','Ñ','N','O','Ó','P','Q','R','S','T','U','Ú','V','W','X','Y','Z']
def accesari():
    try:
        with open('assets/accesari.cfg','r') as f:
            accesari = f.readlines()
            accesari = int(accesari[0])
    except:
        accesari = 0
    accesari += 1
    with open('assets/accesari.cfg','w') as f:
        f.writelines(str(accesari))
    return accesari
accesari = accesari()
def schimba_limba(cod_limba):
    lang = []
    ro=['Limbă','Ajutor','Despre','Alege limba','Română 🇷🇴','Spaniolă 🇪🇸','Litera este la poziția corectă','Litera este la poziția incorectă','Toate literele identice din cuvânt descoperite','Litera nu este în cuvânt','Există',
        'cuvinte din','litere','Glisează pentru a alege mărimea cuvântului','Nu, nu, nu!!! ','Îmi pare rău, nu ai reușit ','să ghicești cuvântul','Cuvântul era:','Ai reușit în ','minut','secunde și',
        'minute','încercări','Felicitări','Verifică','Palabres în','Limbă cuvânt','Engleză 🇬🇧','Atinge pentru un cuvânt nou în ','Opțiuni',
        'Definiții obținute de la: www.dex.ro','Obține litere din cuvânt']

    es=['Idioma','Ayuda','Acerca de','Elige tu idioma','Rumano 🇷🇴','Español 🇪🇸','Letra en la posición correcta','Letra en la posición incorrecta','Todas las letras iguales de la palabra encontradas','La letra no esta en la palabra','Hay',
        'palabras de','letras','Desliza para elegir el tamaño de la palabra','No, no, no!!! ','Lo siento, no has logrado ','encontrar la palabra','La palabra era:','Lo has conseguido en ','minuto','segundos y',
        'minutos', 'intentos','Felicidades','Comprueba','Palabres en','Idioma palabra','Inglés 🇬🇧','Pulsa para una nueva palabra en ','Opciones',
        'Funete definiciones: Diccionario de la lengua española/RAE','Algunas letras de la palabra']
    if cod_limba == 'ro':
        lang=ro
       
    elif cod_limba=='es':
        lang=es
        
    return lang
#creamos la clase Code_show que se encarga de imprimir en pantalla los numeros necesarios de elementos para encontrar la palabra    
class Code_show():
    def __init__(self,lista_caractere,choice,lang, hf,code_check):
                    
        self.choice = choice
        self.lang = lang
        self.code=''
        self.hf=hf
        self.lista_caractere=lista_caractere   
        self.code_check = code_check
        def clear(e):
            self.code_value.value=''
            self.code_value.update()
        self.code_value = ft.TextField(value=self.lista_caractere[0],on_focus=clear,filled =True,color='orange', border_color= 'blue',focused_border_color = 'red', 
                                       max_length=1,capitalization=ft.TextCapitalization.CHARACTERS, text_align=ft.TextAlign.CENTER,keyboard_type = ft.KeyboardType.TEXT, 
                                       text_style=ft.TextStyle(weight=ft.FontWeight.BOLD,),
                                       on_submit=code_check,
                                       input_filter=ft.InputFilter(allow=False, regex_string=r"[0-9]| |,|\*|\\|º|/|\+|<|>|:|;|_|!|@|`|´|¡|'|¿|\?|=|\)|\(|/|&|%$|·|\"|!|ª|#|~|€|¬]|-|{|}|[|]|^|\.]", replacement_string="A"),
                                       height=80,border_width=5,border_radius=40,col={"xs":12/len(self.choice), "md": 12/len(self.choice), "xl":12/len(self.choice)})
    
    def code_minus_click(self, code_value):
        self.hf.heavy_impact()
        self.code_value.value = 'A'
        if self.code_value.value not in self.lista_caractere :
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
        if self.code_value.value not in self.lista_caractere or self.code_value.value is None:
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
                    ft.IconButton(icon_size=50,icon =ft.icons.ARROW_CIRCLE_UP,on_click = lambda *args: self.code_minus_click(self.code_value),width=1000,height=60, style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.colors.RED,ft.ControlState.HOVERED: ft.colors.GREEN,})),
                    self.code_value,
                    ft.IconButton(icon_size=50,icon =ft.icons.ARROW_CIRCLE_DOWN,on_click = lambda *args: self.code_plus_click(self.code_value),width=1000,height=60,style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: ft.colors.GREEN,ft.ControlState.HOVERED: ft.colors.RED,})),
                    ],alignment=ft.MainAxisAlignment.CENTER,col={"xs":12/len(self.choice), "md": 12/len(self.choice), "xl":12/len(self.choice)},)
   
    def code_valor(self):
        if self.code_value.value =='':
            self.code_value.value ='A'
        return self.code_value.value 


def main(page: ft.Page):
    page.title = 'Palabres'
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.HIDDEN
    try:             
        with open('assets/dict.cfg','r') as f:
            cfg = f.readlines()
     
        globals()['color']=cfg[0] 
        ##print(globals()['color'])

        page.theme_mode = ft.ThemeMode.DARK if globals()['color'] == 'DARK' else ft.ThemeMode.LIGHT
        
    except:
        page.theme_mode = ft.ThemeMode.DARK
        globals()['color'] = 'DARK'
    page.spacing=5
    theme = ft.Theme(
        scrollbar_theme=ft.ScrollbarTheme(
        track_color={
            ft.ControlState.HOVERED: ft.colors.TRANSPARENT,
            ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
        },
        track_visibility=True,
        track_border_color=ft.colors.TRANSPARENT,
        thumb_visibility=True,
        thumb_color={
            ft.ControlState.HOVERED: ft.colors.RED,
            ft.ControlState.DEFAULT: ft.colors.TRANSPARENT,
        },
        thickness=10,
        radius=1,
        main_axis_margin=1,
        cross_axis_margin=1,
    )
)
    
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
    
    
    

    def game(lb,mod,lb_cuv):
        start=time.time()
        globals()['count'] = 0
        #page.splash = ft.Row([ft.Text(f'',color=ft.colors.ORANGE,size=20,text_align='center')])
        lang = schimba_limba(lb)
        if lb_cuv =='es':
            lista_caractere = lista_caractere_es
        else :
            lista_caractere = lista_caractere_ro
        
        start_time = None
        start_time = time.time()
        x=mod.split('t')  
        globals()['vieti']=10 +int(x[1])
           
        def alege_cuvantul(litere,lb_cuv):
            lista_cuvinte=[]
            with open(f'./cuv_def/{lb_cuv}_cuv_def{litere}.pkl', 'rb') as fisier:
                defis=pickle.load(fisier)      
            
            lista_cuvinte=list(defis.keys())
            index_selectat = random.randint(0,len(lista_cuvinte)-1)
            choice = lista_cuvinte.pop(index_selectat) 
            defi=defis[choice]#.split('[',maxsplit=1)  
            definitie = defi#[0]
            #print('def',definitie)
            if definitie == 'Vaya,no tengo la definición' or definitie == ' ':
                index_selectat = random.randint(0,len(lista_cuvinte)-1)
                choice = lista_cuvinte.pop(index_selectat) 
                defi=defis[choice]#.split('[',maxsplit=1)  
                definitie = defi#[0].strip() 
            choice=choice.upper()
            nr_cuv=len(defis)      
            #print(choice)
            #print(definitie.strip())
            #print(nr_cuv)
            return choice,definitie,nr_cuv
            
        #choice = alege_cuvantul(x[1],lb_cuv)
        try:
            choice,definitie,nr_cuv = alege_cuvantul(x[1],lb_cuv)
        except: 
            choice,definitie,nr_cuv = game(lb,mod,lb_cuv)
                        
        page.clean()
                    
        '''def menu_item1(*args):            
            def close_dlg(*args):                
                dlg_modal.open = False
                time.sleep(0.1)
                hf.heavy_impact()                           
                page.update()
            def set_limba(lb):
                dlg_modal.open = False
                time.sleep(0.1)
                hf.heavy_impact()
                page.clean()                
                game(lb,mod,lb)
            dlg_modal = ft.AlertDialog(
            modal=False,
            title=ft.Text(lang[3], text_align='center',),
            #content=ft.Text(spans = [ft.TextSpan('Alege limba\n', ft.TextStyle(color=ft.colors.RED, size=18, weight=ft.FontWeight.BOLD,))]),
            actions=[ft.TextButton(lang[4], on_click=lambda e: set_limba('ro')),ft.TextButton(lang[5], on_click=lambda e: set_limba('es')), ],actions_alignment=ft.MainAxisAlignment.CENTER,
               on_dismiss=close_dlg)
            hf.heavy_impact()         
            page.dialog = dlg_modal
            dlg_modal.open = True           
            page.update()
        def menu_item2(*args):
            def close_dlg(*args):                
                dlg_modal.open = False
                time.sleep(0.1)
                hf.heavy_impact()                 
                page.update()
            def set_limba_cuv(lb_cuv):
                hf.heavy_impact()                    
                dlg_modal.open = False
                time.sleep(0.1)
                page.clean()
                game(lb,mod,lb_cuv)
            dlg_modal = ft.AlertDialog(
                modal=False,
                title=ft.Text(lang[26], text_align='center',),
                actions=[ft.TextButton(lang[4], on_click=lambda e: set_limba_cuv('ro')),ft.TextButton(lang[5], on_click=lambda e: set_limba_cuv('es')), ],
                on_dismiss= close_dlg,
                    )
            hf.heavy_impact()        
            page.dialog = dlg_modal
            dlg_modal.open = True           
            page.update()'''
        def menu_item3(*args):
            def close_dlg(*args):                
                dlg_modal.open = False
                time.sleep(0.1)
                hf.heavy_impact()
                page.update()
            dlg_modal = ft.AlertDialog(
                modal=False,
                title=ft.Text(lang[1], text_align='center',),
                content=ft.ResponsiveRow([ft.Text(
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
                        ft.Row([ft.IconButton(ft.icons.HAIL,disabled=True,disabled_color='white'),ft.Text(lang[31], text_align='center',)],ft.MainAxisAlignment.CENTER),
                        ft.Text(f'{lang[30]}',style=ft.TextStyle(color=ft.colors.RED, italic = True,)),
                        ]),
                    actions=[ft.Column([ft.Row([ft.OutlinedButton('Ok', on_click=close_dlg)],ft.MainAxisAlignment.CENTER), ])], 
                    actions_alignment=ft.MainAxisAlignment.CENTER,
                    scrollable=True,
                    on_dismiss=close_dlg,
                    shape=ft.ContinuousRectangleBorder(300)
                    )
                        
            help_dialog = dlg_modal
            hf.heavy_impact()
            dlg_modal.open = True  
            page.overlay.append(help_dialog)         
            page.update()
        def menu_item4(*args):
            def close_dlg(*args):
                dlg_modal.open = False  
                time.sleep(0.1)
                page.update() 
                hf.heavy_impact()
                    
            dlg_modal = ft.AlertDialog(
                modal=False,
                title=ft.Text(lang[2], text_align='center',),
                on_dismiss= close_dlg,
                content=ft.Text(spans= [
                ft.TextSpan('Made with ❤️ by Alexandru G. Muntenas\n'),
                ft.TextSpan('alexandru@muntenas.eu\n',on_click=lambda _:page.launch_url('mailto:alexandru@muntenas.eu'),style=ft.TextStyle(color='red',weight=ft.FontWeight.W_400)),
                ft.TextSpan(f"Flet version: {flet.version.version}\n"),
                ft.TextSpan(f"Visits: {accesari} "),
                ], size=14,italic = True, text_align='center'),actions=[ft.OutlinedButton('Ok', on_click=close_dlg),],
                actions_alignment=ft.MainAxisAlignment.CENTER,
                scrollable=True,
                shape=ft.ContinuousRectangleBorder(300)
                )
                
            about_dialog = dlg_modal
            hf.heavy_impact()
            dlg_modal.open = True
            page.overlay.append(about_dialog)
            page.update()
        
        img = ft.Image(
        src="/icon.png",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

        def set_limba(lb):
            page.clean()                
            game(lb,mod,lb)
        cont_count=ft.Container()   
        half_choice_cont = ft.Container()
        def half_choice(e):
            lst=[]
            for x in choice:
                lst.append(x)
            ind=random.randint(0,len(choice)//2)
            pop_lst=[]
            for y in range(len(choice)//2+1):
                pop_lst.append(lst.pop(ind))
            rand_choice = ''
            for lt in pop_lst:
                rand_choice += lt+ ', '
            #print(rand_choice.strip(' ,'))
            half_choice_cont.content = ft.Text(value = f'{lang[1]}: {rand_choice.strip(" ,")}',color=ft.colors.GREEN,size=20,text_align='center')
            #page.overlay.append(ft.Row([ft.Text(choice[:len(choice)//2+1])]))
            globals()['vieti'] -= globals()['vieti']//2 #(len(choice)//2+1)*2
            cont_count.content = ft.Text(f'{lang[22].capitalize()}: {vieti}',color=ft.colors.ORANGE,size=20,text_align='center')
            cont_count.update()
            half_choice_cont.update()    
        page.appbar = ft.AppBar(leading=img,
                         title=ft.PopupMenuButton(icon = ft.icons.MENU_ROUNDED,
                                                                       items=[
                                                #ft.PopupMenuItem(text=lang[0], on_click=menu_item1,icon=ft.icons.LANGUAGE_ROUNDED),                                                
                                                #ft.PopupMenuItem(text=lang[26], on_click=menu_item2,icon=ft.icons.ABC_ROUNDED),
                                                #ft.PopupMenuItem(),  # divider  
                                                ft.PopupMenuItem(text=lang[1], on_click=menu_item3,icon=ft.icons.HELP_ROUNDED),
                                                ft.PopupMenuItem(text=lang[2], on_click=menu_item4,icon=ft.icons.INFO_OUTLINE_ROUNDED),
                                                                                                    
                                                ],tooltip=lang[29]
                                                         ),
                                actions=[
                                    #ft.IconButton(ft.icons.PLAY_CIRCLE,icon_color = ft.colors.RED,icon_size=36, on_click = lambda *args: game(lb,mod,lb_cuv), tooltip=lang[28]),
                                    ft.TextButton(content=ft.Image(src='/es.png'), on_click=lambda e: set_limba('es'), tooltip=str(lang[28])+str(lang[5])),
                                    ft.TextButton(content=ft.Image(src='/ro.png'), on_click=lambda e: set_limba('ro'), tooltip=str(lang[28])+str(lang[4]))
                                        ],
                                )                           
        
        
        #slide buttton
        def handle_change(e):
            
            slider_value.value = f'{lang[11].capitalize()} {int(e.control.value)+3} {lang[12]}'
            hf.heavy_impact()
            x = slider_value.value.split(' ')
            ##print(x[2])
            nr = x[2]
            mod = f'cuvant{x[2]}'            
            page.update()
            game(lb,mod,lb_cuv)

        
        (slider_value := ft.Text(f"{lang[11].capitalize()} {x[1]} {lang[12]}",color=ft.colors.ORANGE,size=20,text_align='center'))
        #page.navigation_bar  = ft.Row([ft.Slider(divisions=10,max=11,active_color=ft.colors.RED,thumb_color=ft.colors.GREEN,value = int(x[1])-3 ,scale = 1.1,on_change=handle_change,tooltip=lang[13]),ft.Row([ft.Text('    ')]),],alignment=ft.MainAxisAlignment.END)
    
        
        page.add(ft.Column([ft.Row([cont_count, ft.IconButton(ft.icons.HAIL,on_click = half_choice, tooltip=lang[31],icon_color='green'),ft.Text(expand=True),
                                    ft.Slider(divisions=10,max=11,active_color=ft.colors.RED,thumb_color=ft.colors.GREEN,value = int(x[1])-3 ,scale = 1.1,on_change=handle_change,tooltip=str(lang[13])),
                                    ft.Text('')]),
                                    ft.Row([half_choice_cont,ft.Text(expand=True),slider_value,ft.Text(nr_cuv,color = ft.colors.RED,size=20)],alignment=ft.MainAxisAlignment.END)
                                    ],col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},),)
        ##print(len(choice)).
        ''' with open('./palabres.cfg','w') as cfg:
            conf = f'{lb},{mod},{lb_cuv}'
            cfg.writelines(conf)'''
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
        
          
          
        cont_count.content = ft.Text(f'{lang[22].capitalize()}: {vieti}',color=ft.colors.ORANGE,size=20,text_align='center') 
        def increment():
            globals()['count'] += 1 
            globals()['vieti'] -= 1
            cont_count.content = ft.Text(f'{lang[22].capitalize()}: {vieti}',color=ft.colors.ORANGE,size=20,text_align='center')
            
            #splash = ft.Row([ft.Text(f'{lang[22].capitalize()}: ',color=ft.colors.ORANGE,size=20,text_align='center'),cont_count.content])
            
            
            
            
        def code_check(*args):
            hf.heavy_impact()
            hf.heavy_impact()
            code=''
            for i in lista:
                code+=i.code_valor()
                           
            ##print(code)
         
            increment()
            if vieti == 0:
                def close_dlg(*args):  
                    no_dlg.open = False 
                    time.sleep(0.1)
                    page.update()
                    hf.heavy_impact()
                    globals()['count'] = 0
                    game(lb,mod,lb_cuv)                                                   
                no_dlg = ft.AlertDialog(modal =True,title=ft.Text(lang[14], text_align='center',size=25),
                    content=ft.Text(spans=(ft.TextSpan(f'{lang[15]} {lang[16]}.\n{lang[17]} '),
                                           ft.TextSpan(choice,style=ft.TextStyle(color=ft.colors.RED)),
                                           ft.TextSpan(f'\n {definitie}')), text_align='center'),
                    actions=[ft.OutlinedButton('Ok', on_click=close_dlg)],
                    actions_alignment=ft.MainAxisAlignment.CENTER,
                    on_dismiss= close_dlg,
                    shape=ft.ContinuousRectangleBorder(300),
                    scrollable=True)
                page.overlay.append(no_dlg) 
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                hf.heavy_impact()
                no_dlg.open = True
                page.update()       
                
                            
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
                time.sleep(0.1)
                page.update()
                hf.heavy_impact()
                globals()['count'] = 0
            stop=time.time()
            durata = stop-start
            minute = durata//60
            secunde = durata - minute*60
            

            if count != 1:           
                msg =ft.Text(spans=(ft.TextSpan(f'{lang[18]} {count} {lang[22]}.\n{lang[17]} '),
                                           ft.TextSpan(choice,style=ft.TextStyle(color=ft.colors.RED)),
                                           ft.TextSpan(f'\n⌛ {minute:02.0f}:{secunde:2.0f}')), text_align='center')
                    
            else:
                msg =ft.Text(spans=(ft.TextSpan(f'{lang[17]} '),
                                           ft.TextSpan(choice,style=ft.TextStyle(color=ft.colors.RED)),
                                           ft.TextSpan(f'\n⌛ {minute:02.0f}:{secunde:2.0f}')), text_align='center')
                
                
                              
            dlg_modal = ft.AlertDialog(modal=True,title=ft.Text(lang[23], text_align='center',),
                                       content=msg,
                actions=[ft.OutlinedButton('Ok', on_click=close_dlg),],
                actions_alignment=ft.MainAxisAlignment.CENTER,
                on_dismiss=lambda e: game(lb,mod,lb_cuv),
                shape=ft.ContinuousRectangleBorder(300),
                scrollable=True)
            page.overlay.append(dlg_modal)
            dlg_modal.open = True
            page.update()
    
        # CONTAINERE REZULTATE
        
        lista=[Code_show(lista_caractere,choice,lang, hf,code_check) for i in range(len(choice))]
        lista_container=[ft.Container(col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)},) for i in range(len(choice))]
        lista_cont_probe = [ft.Container(col={"xs": 12/len(choice), "md": 12/len(choice), "xl":12/len(choice)}) for i in range(len(choice))]#243
        for i in range(len(choice)):  
                lista_cont_probe[i].content = ft.ListView(spacing=1)
                lista_cont_probe[i].scroll = 'always'    
        
        def evnt(e):
            if e.data=='hide' and page.platform == ft.PagePlatform.ANDROID:
                os._exit(1)
            
        page.on_app_lifecycle_state_change = evnt   
        def dark_light(e):
            page.theme_mode =ft.ThemeMode.DARK if globals()['color'] == 'LIGHT' else ft.ThemeMode.LIGHT
            page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.LIGHT_MODE_OUTLINED,mini=True, on_click=dark_light, bgcolor=ft.colors.BLUE) if globals()['color'] == 'LIGHT' else ft.FloatingActionButton(icon=ft.icons.NIGHTLIGHT_OUTLINED,mini=True, on_click=dark_light, bgcolor=ft.colors.BLUE)
                
            page.update()
            
            globals()['color'] = 'DARK' if globals()['color'] == 'LIGHT' else 'LIGHT'
        
            with open('assets/dict.cfg','w') as f:
                f.writelines(str(globals()['color']))
        if globals()['color'] =='DARK':
            page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.LIGHT_MODE_OUTLINED,mini=True, on_click=dark_light, bgcolor=ft.colors.BLUE)  
        else:
            page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.NIGHTLIGHT_OUTLINED,mini=True, on_click=dark_light, bgcolor=ft.colors.BLUE)
               
        #page.show_snack_bar(ft.SnackBar(content=ft.Text(definitie)))
        page.add(   
              
            ft.ResponsiveRow([ft.Text(definitie,color=ft.colors.BLUE,size = 16)],alignment=ft.MainAxisAlignment.CENTER),     
            ft.ResponsiveRow([i.valor() for i in lista],alignment=ft.MainAxisAlignment.CENTER,col={"xs":12/len(choice), "md": 12/len(choice), "xl":12/len(choice)}),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton(text=lang[24],color='blue', icon='check', icon_color='orange',scale=1.5,on_click=code_check)],alignment=ft.MainAxisAlignment.CENTER,col={"xs": 12/len(choice), "md": 12/len(choice)}), 
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([],alignment=ft.MainAxisAlignment.CENTER),      
            ft.ResponsiveRow([i for i in lista_container],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([i for i in lista_cont_probe],alignment=ft.MainAxisAlignment.CENTER),           
                    
        )
    '''def get_ip():
        response = requests.get('https://api64.ipify.org?format=json').json()
        return response["ip"]


    def get_location():
        ip_address = get_ip()
        response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
        
        country = response.get("country_name")
        return country


    
    country = get_location()
    if country == 'España':game('es', 'cuvant5', 'es')
    elif country == 'Romania':game('ro', 'cuvant5', 'ro')
    else :''' 
    game('es', 'cuvant5', 'es')    
    '''try:
        with open('./palabres.cfg','r') as cfg:
            cfg = cfg.readline().split(',')
            #print(cfg)
            lb = cfg[0]
            mod= cfg[1]
            lb_cuv = cfg[2]
        game(lb,mod,lb_cuv)    
    except: 
        def close_dlg_es(*args):                
                dlg_modal.open = False
                hf.heavy_impact()                           
                page.update()
                game('es', 'cuvant5', 'es')   
        def close_dlg_ro(*args):                
                dlg_modal.open = False
                hf.heavy_impact()                           
                page.update()
                game('ro', 'cuvant5', 'ro')         
        msg =ft.Text(f'Limba / Idioma', text_align='center')
        dlg_modal = ft.AlertDialog(modal=True,title=ft.Text(f'Limba / Idioma', text_align='center',),content=msg,
        actions=[ft.TextButton('Română 🇷🇴', on_click=close_dlg_ro),ft.TextButton('Español 🇪🇸', on_click=close_dlg_es),],
        actions_alignment=ft.MainAxisAlignment.END,)
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()'''
  
    #game('ro', 'cuvant5', 'ro')
ft.app(target=main,view=ft.AppView.WEB_BROWSER)
#ft.app(target=main,view=ft.AppView.WEB_BROWSER) #view=ft.AppView.WEB_BROWSER, 
