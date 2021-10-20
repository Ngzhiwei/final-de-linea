from tkinter import *
from tkinter import ttk
from random import randint
from time import sleep
import serial

root = Tk()
root.title("Ensayos")

estilo = ttk.Style()
estilo.theme_use('default')
estilo.configure("green.Horizontal.TProgressbar", foreground='green', background='green', thickness=70)

root.geometry('700x300')

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

def VentanaAggProducto():
    AggProducto = Toplevel(root)
    AggProducto.title("Agregar producto")
    AggProducto.geometry("250x325")
    Marca = Entry(AggProducto)
    Modelo = Entry(AggProducto)
    Descripcion = Entry(AggProducto)
    PotenciaN = Entry(AggProducto)
    Tension = Entry(AggProducto)
    CorrienteM = Entry(AggProducto)
    Frecuencia = ttk.Combobox(AggProducto, state='readonly')
    Frecuencia['values'] = ('50Hz','60Hz')
    Clase = ttk.Combobox(AggProducto, state='readonly')
    Clase['values'] = ('Clase 1', 'Clase 2')

    Marcalbl = Label(AggProducto, text='Marca:', width=11, anchor='w', pady=10).grid(row=1, column=0)
    Modelolbl = Label(AggProducto, text='Modelo:', width=11, anchor='w', pady=10).grid(row=2, column=0)
    Descripcionlbl = Label(AggProducto, text='Descripcion:', width=11, anchor='w', pady=10).grid(row=3, column=0)
    PotenciaNlbl = Label(AggProducto, text='Potencia Nom.:', width=11, anchor='w', pady=10).grid(row=4, column=0)
    Tensionlbl = Label(AggProducto, text='Tension:', width=11, anchor='w', pady=10).grid(row=5, column=0)
    CorrienteMlbl = Label(AggProducto, text='Corriente Max.:', width=11, anchor='w', pady=10).grid(row=6, column=0)
    Frecuencialbl = Label(AggProducto, text='Frecuencia:', width=11, anchor='w', pady=10).grid(row=7, column=0)
    Claselbl = Label(AggProducto, text='Clase:', width=11, anchor='w', pady=10).grid(row=8, column=0)
    
    Marca.grid(row=1, column=1)
    Modelo.grid(row=2, column=1)
    Descripcion.grid(row=3, column=1)
    PotenciaN.grid(row=4, column=1)
    Tension.grid(row=5, column=1)
    CorrienteM.grid(row=6, column=1)
    Frecuencia.grid(row=7, column=1)
    Clase.grid(row=8, column=1)




barramenu = Menu(root)
root.config(menu=barramenu)

productmenu = Menu(barramenu, tearoff=0)

barramenu.add_cascade(label="Productos", menu=productmenu)

productmenu.add_command(label="Agregar Producto", command=VentanaAggProducto)
productmenu.add_command(label="Eliminar Producto")

botonon = 'yellow'
botonoff = '#F0F0F0'

separador0 = Label(root, text='  ').grid(row=0, column=0)
separador1 = Label(root, text='                                                            ').grid(row=1, column=0)
separador2 = Label(root, text='  ').grid(row=2, column=3)
separador3 = Label(root, text='  ').grid(row=2, column=5)
separador4 = Label(root, text='  ').grid(row=2, column=7)
separador5 = Label(root, text='  ').grid(row=2, column=9)

boton1 = Button(root, text='Corriente', bg=botonoff, padx='12px', pady='5px', command=lambda: Presionado(boton1))
boton2 = Button(root, text='Potencia', bg=botonoff, padx='12px', pady='5px', command=lambda: Presionado(boton2))
boton3 = Button(root, text="""Rigidez
dieléctrica""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton3))
boton4 = Button(root, text="""Puesta
a tierra""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton4))
boton5 = Button(root, text="""Corriente 
de fuga""", bg=botonoff, padx='12px', pady='0px', command=lambda: Presionado(boton5))

barra1 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical', value=50, length=150)
barra2 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical', length=150)
barra3 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical', length=150)
barra4 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical', length=150)
barra5 = ttk.Progressbar(root, style='green.Horizontal.TProgressbar', orient='vertical', length=150)

variable_clase = StringVar()
clase = ttk.Combobox(root, textvariable=variable_clase, state='readonly')
clase['values'] = ('Clase 1', 'Clase 2')
clase.bind('<<ComboboxSelected>>', CambioClase)

clase.place(x=30, y=30)

barra1.grid(row=1, column=2)
boton1.grid(row=2, column=2)
barra2.grid(row=1, column=4)
boton2.grid(row=2, column=4)
barra3.grid(row=1, column=6)
boton3.grid(row=2, column=6)
barra4.grid(row=1, column=8)
boton4.grid(row=2, column=8)
barra5.grid(row=1, column=10)
boton5.grid(row=2, column=10)

root.mainloop()
