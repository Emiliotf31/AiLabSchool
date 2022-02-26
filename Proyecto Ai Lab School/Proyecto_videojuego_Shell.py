from menu_modos import *
#from escenario_pelea import val_id_inic
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox as mss
import tkinter.font as tkFont
import os
from leer_escribir import *

##----------------- VARIABLES GLOBALES
id_inic=''
password=''
id_reg=''
password_reg=''
password_regconf=''
personaje=0
nivel=0

dir_imag="./imagenes/"
AQUARDER_IM= Image.open(dir_imag+"firesor.png")
newsize = (250,250)

ventana=Tk()
ventana.geometry("1450x750")
ventana.title("VIDEOJUEGO")
ventana.config(bg="#46b0f5")



#"{0}x{1}".format(ventana.winfo_screenwidth(), ventana.winfo_screenheight())
#print(ventana.winfo_screenwidth()) #1536
#print(ventana.winfo_screenheight()) #864

Titulo=Label(ventana,text="NOMBRE DEL VIDEOJUEGO",width=25,
             height=5, bg="#f6efe6", font="Ubuntu 30 bold")
Titulo.place(x=440,y=100)
Titulo.config(bg="#46b0f5")


def inic_sesi():
    for widget in ventana.winfo_children():
        widget.destroy()
        
    ventana.title("Inicio de Sesión")
    
    id_lab=Label(ventana,text="Usuario",width=10, height=1,
                 bg="#46b0f5", font="Ubuntu 23 bold")
    id_lab.place(x=650,y=180)
    global id_inic
    id_inic=Entry(ventana,width=25, font="Ubuntu 15 normal")
    id_inic.place(x=608,y=220)
    
    pw_lab=Label(ventana,text="Contraseña",width=10, height=1,
                 bg="#46b0f5",font="Ubuntu 23 bold")
    pw_lab.place(x=650,y=300)
    pw_lab.config(bg="#46b0f5")
    global password
    password=Entry(ventana,width=25, font="Ubuntu 15 normal")
    password.place(x=608,y=340)
    
    b_inic = Button(ventana, text="Iniciar Sesión",width=20, height=2,
                    font="Ubuntu 15 normal",activebackground="#369a61",border=0,command=Val)
    b_inic.place(x=640,y=470)
    
    
    
    
    
def new_user():
    for widget in ventana.winfo_children():
        widget.destroy()
        
    ventana.title("Registro de Usuario Nuevo")
    id_lab_reg=Label(ventana,text="Usuario",width=10, height=1, bg="#46b0f5",
                     font="Ubuntu 23 bold")
    id_lab_reg.place(x=650,y=150)
    global id_reg
    id_reg=Entry(ventana,width=25, font="Ubuntu 15 normal")
    id_reg.place(x=608,y=190)
    
    pw_lab_reg=Label(ventana,text="Contraseña",width=10, height=1, bg="#46b0f5",
                     font="Ubuntu 23 bold")
    pw_lab_reg.place(x=650,y=270)
    global password_reg
    password_reg=Entry(ventana,width=25, font="Ubuntu 15 normal")
    password_reg.place(x=608,y=310)
    
    pw_lab_reg=Label(ventana,text="Confirmar Contraseña",width=20, height=1, bg="#46b0f5",
                     font="Ubuntu 23 bold")
    pw_lab_reg.place(x=558,y=390)
    global password_regconf
    password_regconf=Entry(ventana,width=25, font="Ubuntu 15 normal")
    password_regconf.place(x=608,y=430)

    b_reg = Button(ventana, text="Registrar Nuevo Usuario", width=25, height=2,
                   font="Ubuntu 15 normal",activebackground="#369a61",border=0,command=Reg_new_user)
    b_reg.place(x=607,y=530)

    b_inic = Button(ventana, text="Iniciar Sesión",width=20, height=2,
                    font="Ubuntu 15 normal",activebackground="#369a61",border=0,command=inic_sesi)
    b_inic.place(x=90,y=600)
    
    
    
def Val():
    ##loadedData = leer_csv(path="fakeBd.csv")
    
    user_act=[["Usuario"],[id_inic.get()]]
    
    x = id_inic.get()
    y = password.get()
    data=x+".csv"
    direc="./Registros_usuarios/"+data
    find_user=os.path.exists(direc)
    if find_user == False:
        #ventana.config(bg="#D61C1F") # editar el background
        valor=mss.askyesno(message="No existe ningún usuario con ese nombre. ¿Desea crear uno nuevo?",title="Pregunta")
        if valor == True:
           new_user()
        else:
            id_inic.delete(0, END)
            password.delete(0, END)
    else:
        if y == leer_csv(path=direc)[2][1]:
            escribir_csv(user_act, path="./Registros_usuarios/Usuario_Actual.csv")
            modo_juego(ventana,id_inic)
            #val_id_inic(id_inic_v)
        else:
            mss.showerror(message="Contraseña Incorrecta", title="Error")
            password.delete(0,END)
            

def Reg_new_user():
    user_act=[["Usuario"],[id_reg.get]]
    usuario=id_reg.get()
    pw=password_reg.get()
    pw_conf=password_regconf.get()
    user=[['Usuario','Contraseña','Personaje','Nivel'],[usuario,pw,personaje,nivel]]
    
    x = id_reg.get()+".csv"
    direc="./Registros_usuarios/"+x
    find_user=os.path.exists(direc)
    if find_user == False:
        if pw == pw_conf:
            #file=id_reg.get()+".csv"
            escribir_csv(user, path=direc)
            mss.showinfo(message=x+" ha sido registrado.\nInicia Sesión", title="Registro")
            escribir_csv(user_act, path="./Registros_usuarios/Usuario_Actual.csv")
            modo_juego(ventana,id_reg)
        else:
            mss.showerror(message="Las contraseñas deben ser iguales", title="Error")
    else:
        mss.showerror(message="No se puede continuar debido a que ya existe\nuna sesión registrada con ese usuario.\nIntente nuevamente con otro usuario.", title="Error")
        id_reg.delete(0, END)
        password_reg.delete(0, END)
        password_regconf.delete(0, END)



login=Button(ventana,text="Iniciar Sesión",width=20, height=2, bg="#f6efe6",
             font="Ubuntu 15 normal",activebackground="#369a61",border=0,command=inic_sesi)
login.place(x=640,y=380)

new_user_reg=Button(ventana,text="Usuario Nuevo",width=20, height=2, bg="#f6efe6",
                    font="Ubuntu 15 normal", activebackground="#369a61",
                    border=0,command=new_user)  #height=1,width=15
new_user_reg.place(x=640,y=480)



ventana.mainloop()
