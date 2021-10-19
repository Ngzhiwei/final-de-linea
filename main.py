from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
import serial

root = Tk()

estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("green.Horizontal.TProgressbar", foreground='green', background='green')

root.geometry('700x300')

barramenu = Menu(root)
root.config(menu=barramenu)

filemenu = Menu(barramenu)
editmenu = Menu(barramenu)
helpmenu = Menu(barramenu)

barramenu.add_cascade(label="Archivo", menu=filemenu)
barramenu.add_cascade(label="Editar", menu=editmenu)
barramenu.add_cascade(label="Ayuda", menu=helpmenu)

botonon = 'yellow'
botonoff = '#F0F0F0'

def Presionado(btn):
    if btn['bg'] == botonoff:
        btn.config(bg=botonon)
    else:
        btn.config(bg=botonoff)

def CambioClase(event):
    if clase.get() == 'Clase 2':
        boton4.config(state='disabled', bg=botonoff)
        boton5.config(state='disabled', bg=botonoff)
    else:
        boton4.config(state='normal')
        boton5.config(state='normal')


separador1 = Label(root, text='  ').grid(row=3, column=0)
separador2 = Label(root, text='  ').grid(row=2, column=2)
separador3 = Label(root, text='  ').grid(row=2, column=4)
separador4 = Label(root, text='  ').grid(row=2, column=6)
separador5 = Label(root, text='  ').grid(row=2, column=8)

boton1 = Button(root, text='Corriente', bg=botonoff, padx='12px', pady='5px', command=lambda: Presionado(boton1))
boton2 = Button(root, text='Potencia', bg=botonoff, padx='12px', pady='5px', command=lambda: Presionado(boton2))
boton3 = Button(root, text="""Rigidez
dieléctrica""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton3))
boton4 = Button(root, text="""Puesta
a tierra""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton4))
boton5 = Button(root, text="""Corriente 
de fuga""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton5))

barra1 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical')
barra2 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical')
barra3 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical')
barra4 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical')
barra5 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical')

variable_clase = StringVar()
clase = ttk.Combobox(root, textvariable=variable_clase, state='readonly')
clase['values'] = ('Clase 1', 'Clase 2')
clase.bind('<<ComboboxSelected>>', CambioClase)

clase.grid(row=0, column=0)

barra1.grid(row=1, column=1)
boton1.grid(row=2, column=1)
barra2.grid(row=1, column=3)
boton2.grid(row=2, column=3)
barra3.grid(row=1, column=5)
boton3.grid(row=2, column=5)
barra4.grid(row=1, column=7)
boton4.grid(row=2, column=7)
barra5.grid(row=1, column=9)
boton5.grid(row=2, column=9)

root.mainloop()
