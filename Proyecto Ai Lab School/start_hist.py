from menu_modos import *
from checkpoint import comb_entr
from tkinter import *
from PIL import ImageTk, Image
import time
import numpy as np
from tkinter import messagebox as mss
from leer_escribir import *
#import subprocess

blue=['#2e6acc']

dir_imag = "./imagenes/"
AQUARDER_IM= Image.open(dir_imag+"aquarder.png")
ELECTDER_IM= Image.open(dir_imag+"electder.png")
FIRESOR_IM= Image.open(dir_imag+"firesor.png")
MOUSEBUG_IM= Image.open(dir_imag+"mousebug.png")
ROCKDOG_IM= Image.open(dir_imag+"rockdog.png")
SPLANT_IM= Image.open(dir_imag+"splant.png")
newsize = (250,250)

CUADRADO_IM= Image.open(dir_imag+"cuadrado.jpg")
CUADRADO_A_IM= Image.open(dir_imag+"cuadrado_a.jpg")
c = (1340,15)
DIAL_IM= Image.open(dir_imag+"dialog.png")
d = (450,250)

hist_selec=Tk()
hist_selec.geometry("1450x750")
hist_selec.title("MODO HISTORIA - NOMBRE DEL VIDEOJUEGO")
hist_selec.config(bg="#46b0f5")

direc="./Registros_usuarios/Usuario_Actual.csv"
usuario=leer_csv(path=direc)[2][0]
path="./Registros_usuarios/"+usuario+".csv"
if int(leer_csv(path=path)[2][2]) == 0:
    mss.showinfo(message="¡Bienvenido! Ahora estás en modo historia. Para esta modalidad debes escoger a tu personaje para que combatas con todos los demás aquí mencionados. Una vez que derrotes a todos terminarás el juego. Podrás guardar tu avance cada vez que acabes una batalla. ¡BUENA SUERTE!",title="Instrucciones")


## 46b0f5

def selec(pers):
    ls=["aquarder","electder","firesor","mousebug","rockdog","splant"]
    
    colors=[]

    for i in range(len(ls_im)):
        color=ls_im[i].cget('bg')
        colors.append(color)
        
    colors_blue = list(filter(lambda a: a=='#2e6acc',colors))
    #colors_red = list(filter(lambda a: a=='red',colors))

    if colors_blue != blue:
        for i in range(len(ls_im)):
            if pers == ls[i]:
                ls_im[i].config(bg="#2e6acc")
                if i == 0:
                    ls_0=ls_im[1:]
                    for j in range(len(ls_0)):
                        ls_0[j].config(bg="#65a95f")
                elif i != 0:
                    ls_menor=ls_im[:i]
                    for k in range(len(ls_menor)):
                        ls_menor[k].config(bg="#65a95f")
                    ls_mayor=ls_im[i+1:]
                    for l in range(len(ls_mayor)):
                        ls_mayor[l].config(bg="#65a95f")
                
    elif colors_blue == blue:
        for i in range(len(ls_im)):
            if pers == ls[i] and ls_im[i].cget('bg')=='#2e6acc':
                ls_im[i].config(bg="#65a95f")

    hist_selec.update()

def det(det_pers):
    ls_det=["aq","el","fi","mo","ro","sp"]
    ls_pim
    ls_tipo = ["Aquarder","Electder","Firesor","Mousebug","Rockdog","Splant"]
    ls_descrp = [["Tipo: Agua","Ventaja contra: Roca, Fuego"
                      ,"Desventaja contra: Eléctrico, Planta",
                      "Normal contra: Agua, Escarabajo"],
                 ["Tipo: Eléctrico","Ventaja contra: Agua, Escarabajo"
                  ,"Desventaja contra: Roca, Planta",
                  "Normal contra: Eléctrico, Fuego"],
                 ["Tipo: Fuego","Ventaja contra: Planta, Escarabajo"
                  ,"Desventaja contra: Agua, Roca",
                  "Normal contra: Eléctrico, Fuego"],
                 ["Tipo: Escarabajo","Ventaja contra: Planta, Roca"
                  ,"Desventaja contra: Fuego, Eléctrico",
                  "Normal contra: Escarabajo, Agua"],
                 ["Tipo: Roca","Ventaja contra: Fuego, Eléctrico"
                  ,"Desventaja contra: Agua, Planta",
                  "Normal contra: Roca, Escarabajo"],
                 ["Tipo: Planta","Ventaja contra: Roca, Agua, Eléctrico"
                  ,"Desventaja contra: Fuego, Escarabajo",
                  "Normal contra: Planta"]]
    global ls_esp,ls_ataq1,ls_ataq2,ls_pot
    ls_esp = ["Aqua-jet","Trueno",
              "Llamarada","Picotazo",
              "Roca afilado","Hoja Navaja"]
    ls_ataq1 = ["Cola férrea","Arañazo","Embestida","Embestida","Velocidad","Mordisco"]
    ls_ataq2 = ["Cabezazo","Mordisco","Mordisco","Cabezazo","Cola férrea","Cabezazo"]
    ls_pot = ["Lluvia","Campo Magnético",
              "Día Soleado","Esporas",
              "Campo Rocoso","Rayo Solar"]
    global ls_habilidades
    ls_habilidades=[ls_esp,ls_ataq1,ls_ataq2,ls_pot]
    
    new_width=18
    
    det = Toplevel(hist_selec)
    

    for j in range(len(ls_det)):
        if det_pers==ls_det[j]:
            det.geometry("900x400")
            det.title("DESCRIPCIÓN DEL PERSONAJE")
            det.config(bg="#46b0f5")
            
            pers = Label(det, image=ls_pim[j])
            pers.place(x=40,y=75)

            ## ------- DESCRIPCIÓN DEL PERSONAJE

            tipo = Label(det, text=ls_tipo[j],
                         font="Ubuntu 15 bold",bg="#46b0f5")
            tipo.place(x=550,y=30)
            pos_descrp = [60,90,120,150]
            descrp = ls_descrp[j]
            for i in range(len(pos_descrp)):
                tipo = Label(det, text=descrp[i],
                         font="Ubuntu 12 bold",bg="#46b0f5")
                tipo.place(x=400,y=pos_descrp[i])

            ## ------- TABLA DE LOS PUNTOS DE ATAQUES NORMALES

            pos_reng_1 = [315,460,598,737]
            reng_1 = ["Habilidad","Ataque Normal"
                      ,"Ataque Ventaja",
                      "Ataque Desventaja"]
            for i in range(len(pos_reng_1)):
                x11 = Label(det, text=reng_1[i],width=new_width,
                         font="Ubuntu 10 normal",bg="#47923b",relief="solid")
                x11.place(x=pos_reng_1[i],y=185)

            reng_2 = [ls_esp[j],"3 puntos"
                      ,"5 puntos",
                      "2 puntos"]
            for i in range(len(pos_reng_1)):
                if reng_2[i] == ls_esp[j]:
                    x11 = Label(det, text=reng_2[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#47923b",relief="solid")
                    x11.place(x=pos_reng_1[i],y=205)
                else:
                    x11 = Label(det, text=reng_2[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#2bb016",relief="solid")
                    x11.place(x=pos_reng_1[i],y=205)
                

            reng_3 = [ls_ataq1[j],"2 puntos"
                      ,"NA","NA"]
            for i in range(len(pos_reng_1)):
                if reng_3[i] == ls_ataq1[j]:
                    x11 = Label(det, text=reng_3[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#47923b",relief="solid")
                    x11.place(x=pos_reng_1[i],y=225)
                else:
                    x11 = Label(det, text=reng_3[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#2bb016",relief="solid")
                    x11.place(x=pos_reng_1[i],y=225)


            reng_4 = [ls_ataq2[j],"2 puntos"
                      ,"NA","NA"]
            for i in range(len(pos_reng_1)):
                if reng_4[i] == ls_ataq2[j]:
                    x11 = Label(det, text=reng_4[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#47923b",relief="solid")
                    x11.place(x=pos_reng_1[i],y=245)
                else:
                    x11 = Label(det, text=reng_4[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#2bb016",relief="solid")
                    x11.place(x=pos_reng_1[i],y=245)


            ## ------- POTENCIADOR DEL PERSONAJE

            x11 = Label(det, text="POTENCIADOR: Aumenta en +2 puntos los puntos de ataque la habilidad especial."
                         ,font="Ubuntu 10 bold",bg="#46b0f5",fg='#951919')
            x11.place(x=315,y=275)
            x11 = Label(det, text="Solo se puede utilizar una vez cada 3 turnos y dura 2 turnos."
                         ,font="Ubuntu 10 bold",bg="#46b0f5",fg='#951919')
            x11.place(x=315,y=293)

            x11 = Label(det, text=ls_pot[j],width=71,
                        font="Ubuntu 10 normal",bg="#b91212",relief="solid")
            x11.place(x=314,y=320)
                
            for i in range(len(pos_reng_1)):
                x11 = Label(det, text=reng_1[i],width=new_width,
                         font="Ubuntu 10 normal",bg="#b91212",relief="solid")
                x11.place(x=pos_reng_1[i],y=340)
                
            reng_5 = [ls_esp[j],"5 puntos"
                      ,"7 puntos",
                      "4 puntos"]
            for i in range(len(pos_reng_1)):
                if reng_2[i] == ls_esp[j]:
                    x11 = Label(det, text=reng_5[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#b91212",relief="solid")
                    x11.place(x=pos_reng_1[i],y=360)
                else:
                    x11 = Label(det, text=reng_5[i],width=new_width,
                             font="Ubuntu 10 normal",bg="#e53d3d",relief="solid")
                    x11.place(x=pos_reng_1[i],y=360)

            det.mainloop()


def combatir():
    ls_esp = ["Aqua-jet","Trueno",
              "Llamarada","Picotazo",
              "Roca afilado","Hoja Navaja"]
    ls_ataq1 = ["Cola férrea","Arañazo","Embestida","Embestida","Velocidad","Mordisco"]
    ls_ataq2 = ["Cabezazo","Mordisco","Mordisco","Cabezazo","Cola férrea","Cabezazo"]
    ls_pot = ["Lluvia","Campo Magnético",
              "Día Soleado","Esporas",
              "Campo Rocoso","Rayo Solar"]
    ls_habilidades=[ls_esp,ls_ataq1,ls_ataq2,ls_pot]
    colors=[]
    for i in range(len(ls_im)):
        color=ls_im[i].cget('bg')
        colors.append(color)
    
    colors_blue = list(filter(lambda a: a=='#2e6acc',colors))

    if colors_blue!=['#2e6acc']:
        mss.showerror(message="Elija a su personaje", title="Error")
    else:
        pos_per=colors.index('#2e6acc')+1
        print(pos_per)
        direc="./Registros_usuarios/Usuario_Actual.csv"
        usuario=leer_csv(path=direc)[2][0]
        path="./Registros_usuarios/"+usuario+".csv"
        f_d=leer_csv(path=path)
        f_d[2][2]=pos_per
        f_d[2][3]=1
        #pos_cpu=f_d[2][3]
        new_pers=list(filter(lambda a: a != [],f_d))
        escribir_csv(new_pers,path=path)
        #escribir_csv(new_pers,path=path)
        mss.showinfo(message="Tu personaje se ha guardado. Prepárate para tu primera pelea.",title="Preparado para la batalla")
        comb_entr(pos_per,hist_selec,ls_pim,ls_decor,ls_habilidades)

def cont():
    ls_esp = ["Aqua-jet","Trueno",
              "Llamarada","Picotazo",
              "Roca afilado","Hoja Navaja"]
    ls_ataq1 = ["Cola férrea","Arañazo","Embestida","Embestida","Velocidad","Mordisco"]
    ls_ataq2 = ["Cabezazo","Mordisco","Mordisco","Cabezazo","Cola férrea","Cabezazo"]
    ls_pot = ["Lluvia","Campo Magnético",
              "Día Soleado","Esporas",
              "Campo Rocoso","Rayo Solar"]
    ls_habilidades=[ls_esp,ls_ataq1,ls_ataq2,ls_pot]
    direc="./Registros_usuarios/Usuario_Actual.csv"
    usuario=leer_csv(path=direc)[2][0]
    path="./Registros_usuarios/"+usuario+".csv"
    pos_per=int(leer_csv(path=path)[2][2])
    comb_entr(pos_per,hist_selec,ls_pim,ls_decor,ls_habilidades)
             

aquarder_im = ImageTk.PhotoImage(AQUARDER_IM.resize(newsize))
electder_im = ImageTk.PhotoImage(ELECTDER_IM.resize(newsize))
firesor_im = ImageTk.PhotoImage(FIRESOR_IM.resize(newsize))
mousebug_im = ImageTk.PhotoImage(MOUSEBUG_IM.resize(newsize))
rockdog_im = ImageTk.PhotoImage(ROCKDOG_IM.resize(newsize))
splant_im = ImageTk.PhotoImage(SPLANT_IM.resize(newsize))
ls_pim=[aquarder_im,electder_im,firesor_im,mousebug_im,rockdog_im,splant_im]

cuadrado_im = ImageTk.PhotoImage(CUADRADO_IM.resize(c))
cuadrado_a_im = ImageTk.PhotoImage(CUADRADO_A_IM.resize(c))
dialog_im = ImageTk.PhotoImage(DIAL_IM.resize(d))
ls_decor=[cuadrado_im,cuadrado_a_im,dialog_im]


select_aquarder = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                         command=lambda:selec("aquarder"))
select_aquarder.place(x=150,y=60)
select_aquarder.config(image=aquarder_im)
detail_aquarder = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("aq"))
detail_aquarder.place(x=208,y=325)


select_electder = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                        command=lambda:selec("electder"))
select_electder.place(x=460,y=60)
select_electder.config(image=electder_im)
detail_electder = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("el"))
detail_electder.place(x=518,y=325)


select_firesor = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                        command=lambda:selec("firesor"))
select_firesor.place(x=770,y=60)
select_firesor.config(image=firesor_im)
detail_firesor = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("fi"))
detail_firesor.place(x=828,y=325)


select_mousebug = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                        command=lambda:selec("mousebug"))
select_mousebug.place(x=150,y=410)
select_mousebug.config(image=mousebug_im)
detail_mousebug = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("mo"))
detail_mousebug.place(x=208,y=675)


select_rockdog = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                        command=lambda:selec("rockdog"))
select_rockdog.place(x=460,y=410)
select_rockdog.config(image=rockdog_im)
detail_rockdog = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("ro"))
detail_rockdog.place(x=518,y=675)


select_splant = Button(hist_selec, activebackground="#6f6c65",bg="#65a95f",
                        command=lambda:selec("splant"))
select_splant.place(x=770,y=410)
select_splant.config(image=splant_im)
detail_splant = Button(hist_selec, text="Detalles", width=12, height=1,
                         font="Ubuntu 15 normal",activebackground="#6f6c65"
                         ,border=0,command=lambda:det("sp"))
detail_splant.place(x=828,y=675)

direc="./Registros_usuarios/Usuario_Actual.csv"
usuario=leer_csv(path=direc)[2][0]
path="./Registros_usuarios/"+usuario+".csv"

if int(leer_csv(path=path)[2][3])==0:
    b_reg = Button(hist_selec, text="EMPEZAR HISTORIA", width=20, height=2,
                   font="Ubuntu 20 normal",activebackground="#ca9e20"
                   ,relief=RAISED,command=combatir,bg="#c7ca20")
    b_reg.place(x=1080,y=230)

if int(leer_csv(path=path)[2][3])>0:
    b_reg = Button(hist_selec, text="CONTINUAR HISTORIA", width=20, height=2,
                   font="Ubuntu 20 normal",activebackground="#ca9e20"
                   ,relief=RAISED,command=cont,bg="#c7ca20")
    b_reg.place(x=1085,y=230)
    
per = Label(hist_selec, text="AZUL ES SU PERSONAJE",width=25,height=2
            ,font="Ubuntu 12 bold",bg="#2e6acc",fg='#000d74')
per.place(x=1120,y=400)

ls_im=[select_aquarder,select_electder,select_firesor,select_mousebug,select_rockdog,select_splant]

def handler():
    direc="./Registros_usuarios/Usuario_Actual.csv"
    id_inic=leer_csv(path=direc)[2][0]
    modo_juego(hist_selec,id_inic)
        
hist_selec.protocol("WM_DELETE_WINDOW", handler)
hist_selec.mainloop()

