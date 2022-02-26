##from Proyecto_videojuego_Shell import val_id_inic
from tkinter import *
from PIL import ImageTk, Image
from CPU_ataq import ataq_hp

ls_esp = ["Aqua-jet","Trueno",
          "Llamarada","Picotazo",
          "Roca afilado","Hoja Navaja"]
ls_ataq1 = ["Cola férrea","Arañazo","Embestida","Embestida","Velocidad","Mordisco"]
ls_ataq2 = ["Cabezazo","Mordisco","Mordisco","Cabezazo","Cola férrea","Cabezazo"]
ls_pot = ["Lluvia","Campo Magnético",
          "Día Soleado","Esporas",
          "Campo Rocoso","Rayo Solar"]
ls_habilidades=[ls_esp,ls_ataq1,ls_ataq2,ls_pot]

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

def comb_entr(pos_per,pos_cpu,entrena,ls_pim,ls_decor,ls_habilidades):
    for i in range(len(ls_pim)):
        if pos_per == i:
            pers_im=ls_pim[i]
            habil_esp=ls_habilidades[0][i]
            ataq1=ls_habilidades[1][i]
            ataq2=ls_habilidades[2][i]
            pot=ls_habilidades[3][i]
        if pos_cpu == i:
            cpu_im=ls_pim[i]
            habil_esp_cpu=ls_habilidades[0][i]
            ataq1_cpu=ls_habilidades[1][i]
            ataq2_cpu=ls_habilidades[2][i]
            pot_cpu=ls_habilidades[3][i]

    atq_pers=[habil_esp,ataq1,ataq2,pot]
    atq_cpu=[habil_esp_cpu,ataq1_cpu,ataq2_cpu,pot_cpu]
    
    comb = Toplevel(entrena)
    comb.geometry("1450x750")
    comb.title("COMBATE (MODO ENTRENAMIENTO)")
    comb.config(bg="#46b0f5")
        
    def iniciar():
        iniciar.destroy()
##        id_inic = id_inic_v
        comb.update()
        ataq_hp(comb,pos_per,pos_cpu,hp_cpu_sh,hp_pers_sh,selec_ataq,entrena)

    im_cuadrado = Label(comb,image=ls_decor[0])
    im_cuadrado.place(x=106,y=385)
    im_a_cuadrado = Label(comb,image=ls_decor[1])
    im_a_cuadrado.place(x=0,y=368)

    im_pers = Label(comb,image=pers_im,bg="#2e6acc")
    im_pers.place(x=100,y=50)

    pos_y=[90,131,172,213]
    for i in range(len(atq_pers)):
        selec_ataq = Button(comb, text=atq_pers[i], width=20, height=1,
                   font="Ubuntu 15 normal",activebackground="#ca9e20"
                   ,relief=RAISED,bg="#c7ca20",justify=CENTER,command=True)
        selec_ataq.place(x=400,y=pos_y[i])
    
    hp_pers_sh = Label(comb,text="20 HP",font="Ubuntu 28 bold",bg="#2e6acc"
                   ,fg='#000d74',justify=CENTER,relief="solid",
                   height=2,width=12)
    hp_pers_sh.place(x=900,y=125)
    
    im_cpu = Label(comb,image=cpu_im,bg="red")
    im_cpu.place(x=1150,y=450)

    hp_cpu_sh = Label(comb,text="20 HP",font="Ubuntu 28 bold",bg="red"
                   ,fg='#850000',justify=CENTER,relief="solid",
                   height=2,width=12)
    hp_cpu_sh.place(x=800,y=520)

    dial = Label(comb,image=ls_decor[2],bg="#46b0f5")
    dial.place(x=100,y=450)

    iniciar = Button(comb, text="INICIAR", width=20, height=2,
                    font="Ubuntu 20 normal",activebackground="#c12665"
                   ,relief=RAISED,bg="#f92a7e",justify=CENTER,command=iniciar)
    iniciar.place(x=550,y=340)

    
    comb.mainloop()
