from tkinter import *
from PIL import ImageTk, Image
import os
import time
import numpy as np

path = os.path.dirname(os.path.realpath('aquader.png'))
print(path)

dir_imag = "./imagenes/"
electder = "./imagenes/electder.png"
firesor = "./imagenes/firesor.png"
mousebug = "./imagenes/mousebug.png"
## mousebug = "C:/Users/emili/Documents/JUPYTER/Proyecto Ai Lab School/imagenes/mousebug.png"

AQUARDER_IM= Image.open(dir_imag+"aquarder.png")
ELECTDER_IM= Image.open(electder)
FIRESOR_IM= Image.open(firesor)
MOUSEBUG_IM= Image.open(mousebug)
newsize = (250,250)
    
entrena=Tk()
entrena.geometry("1450x750")
entrena.title("MODO ENTRENAMIENTO - NOMBRE DEL VIDEOJUEGO")
entrena.config(bg="#46b0f5")

aquarder_im = ImageTk.PhotoImage(AQUARDER_IM.resize(newsize))
electder_im = ImageTk.PhotoImage(ELECTDER_IM.resize(newsize))
firesor_im = ImageTk.PhotoImage(FIRESOR_IM.resize(newsize))


select_aquarder = Button(entrena, activebackground="#2e6acc",bg="#9c9583",
                         command=True)
select_aquarder.place(x=150,y=380)
select_aquarder.config(image=aquarder_im)

select_electder = Button(entrena, activebackground="#2e6acc",bg="red",
                        command=True)
select_electder.place(x=460,y=380)
select_electder.config(image=electder_im)

select_firesor = Button(entrena, activebackground="#2e6acc",bg="#9c9583",
                        command=True)
select_firesor.place(x=770,y=380)
select_firesor.config(image=firesor_im)

ls_im=[select_aquarder,select_electder,select_firesor]


colors=[]

for i in range(len(ls_im)):
    color=ls_im[i].cget('bg')
    colors.append(color)
        #color=[ls_im[i].cget('bg')]

colors = np.array(colors)
colors_arr = np.where(colors == "red", True, False)
print(colors_arr1)



entrena.mainloop()



##from tkinter import *
##from PIL import ImageTk, Image
##import os
##import time
##
##path = os.path.dirname(os.path.realpath('aquader.png'))
##print(path)
##
##dir_imag = "./imagenes/"
##electder = "./imagenes/electder.png"
##firesor = "./imagenes/firesor.png"
##mousebug = "./imagenes/mousebug.png"
#### mousebug = "C:/Users/emili/Documents/JUPYTER/Proyecto Ai Lab School/imagenes/mousebug.png"
##
##AQUARDER_IM= Image.open(dir_imag+"aquarder.png")
##ELECTDER_IM= Image.open(electder)
##FIRESOR_IM= Image.open(firesor)
##MOUSEBUG_IM= Image.open(mousebug)
##newsize = (250,250)
##    
##entrena=Tk()
##entrena.geometry("1450x750")
##entrena.title("MODO ENTRENAMIENTO - NOMBRE DEL VIDEOJUEGO")
##entrena.config(bg="#46b0f5")
##aquarder_im = ImageTk.PhotoImage(AQUARDER_IM.resize(newsize))
##
##select_aquarder = Button(entrena, activebackground="blue", command=selec)
##select_aquarder.place(x=640,y=380)
##select_aquarder.config(image=aquarder_im)
##
##def selec():
##    select_aquarder.config(image=electder_im)
##    entrena.update()
##
##
##entrena.mainloop()
