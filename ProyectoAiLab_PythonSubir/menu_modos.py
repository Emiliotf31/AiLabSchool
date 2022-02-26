##import start_hist
##import checkpoint
import subprocess
from tkinter import *
import tkinter.font as tkFont
##import os
from leer_escribir import *

def modo_juego(ventana,id_inic):
    comp_file=isinstance(id_inic,str)
    if comp_file == False:
        file=id_inic.get()
    else:
        file=id_inic

    ventana.destroy()
    print("crea juego")
    global juego
    juego=Tk()
    juego.geometry("1450x750")
    juego.title("NOMBRE DEL JUEGO")
    juego.config(bg="#6b4b4b")

    b_hist = Button(juego, text="Modo Historia", width=30, height=3, bg="#f6efe6",
                    font="Ubuntu 15 normal", border=0,command=lambda:hist(file)).pack(side=TOP)
    #b_hist.place(x=105,y=80)

    b_entr = Button(juego, text="Modo Entrenamiento", width=30, height=3, bg="#f6efe6",
                    font="Ubuntu 15 normal",border=0, command=entr).pack(side=BOTTOM)
    juego.mainloop()
    #b_entr.place(x=105,y=120)


def entr():
    juego.destroy()
    print("Control_1")
    
    subprocess.call(["python", "modo_entrena.py"])


def hist(file):
    juego.destroy()
    data=file+".csv"
    direc="./Registros_usuarios/"+data
    subprocess.call(["python", "start_hist.py"])
    
