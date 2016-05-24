#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, datetime
from Tkinter import *
from tkFileDialog import *
import ttk
import PIL
from PIL import ImageTk
import archivo, datos, nubes, deteccion
import matplotlib.pyplot as plt
import scipy.misc

# Variables globales
bandas = {}
bandas['rutas'] = {}
bandas['imagenes'] = {}
metadata = {}

def start():
    global val, w, root
    root = Tk()
    top = Ventana(root)
    root.mainloop()

class Ventana:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("800x200+310+76")
        top.title("Erosión en LANDSAT 8")
        top.configure(background="#d9d9d9")

        self.imagen_rgb = ''
        self.imagen_nubes = ''
        self.imagen_ndvi = ''
        self.imagen_erosion = ''

        self.Label1 = Label(top)
        self.Label1.place(relx=0.13, rely=0.03, height=22, width=356)
        self.Label1.configure(background=_bgcolor)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='Detección de erosion a partir de imagenes LANDSAT 8')

        self.Label2 = Label(top)
        self.Label2.place(relx=0.13, rely=0.23, height=22, width=586)
        self.Label2.configure(background=_bgcolor)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='Por favor ingrese la ruta de la carpeta que contiene las imágenes y el archivo de metadata:')

        self.ruta = Entry(top)
        self.ruta.place(relx=0.13, rely=0.43, height=22, width=486)
        self.ruta.configure(background="white")
        self.ruta.configure(font="TkFixedFont")
        self.ruta.configure(foreground="#000000")
        self.ruta.configure(insertbackground="black")
        self.ruta.configure(width=662)

        self.abrir = Button(top, text='Abrir', command=self.abrir)
        self.abrir.place(relx=0.75, rely=0.43, height=28, width=89)
        self.abrir.configure(activebackground="#d9d9d9")
        self.abrir.configure(activeforeground="#000000")
        self.abrir.configure(background=_bgcolor)
        self.abrir.configure(foreground="#000000")
        self.abrir.configure(highlightbackground="#d9d9d9")
        self.abrir.configure(highlightcolor="black")
        self.abrir.configure(width=89)

        self.Enviar = Button(top, text='Aceptar', command=self.enviar)
        self.Enviar.place(relx=0.75, rely=0.73, height=28, width=89)
        self.Enviar.configure(activebackground="#d9d9d9")
        self.Enviar.configure(activeforeground="#000000")
        self.Enviar.configure(background=_bgcolor)
        self.Enviar.configure(foreground="#000000")
        self.Enviar.configure(highlightbackground="#d9d9d9")
        self.Enviar.configure(highlightcolor="black")
        self.Enviar.configure(width=89)

        self.Descargar = Button(top, text='Descargar', command=self.descargar)
        self.Descargar.place(relx=0.60, rely=0.73, height=28, width=89)
        self.Descargar.configure(activebackground="#d9d9d9")
        self.Descargar.configure(activeforeground="#000000")
        self.Descargar.configure(background=_bgcolor)
        self.Descargar.configure(foreground="#000000")
        self.Descargar.configure(highlightbackground="#d9d9d9")
        self.Descargar.configure(highlightcolor="black")
        self.Descargar.configure(width=89)

    def abrir(self):
        directory = askdirectory(parent=root)
        self.ruta.delete(0,END)
        self.ruta.insert(0,directory)

    def enviar(self):
        if os.path.exists(self.ruta.get()) and os.path.isdir(self.ruta.get()):
            archivo.darArchivo(bandas,metadata,self.ruta.get())
        else:
            popup = Toplevel()
            popup.geometry("300x100+575+126")
            label1 = Label(popup, text='Por favor ingrese una ruta válida', height=5, width=50)
            label1.pack()

        print ':: Obteniendo datos %s ::' % (datetime.datetime.utcnow())
        datos.obtenerDatos(metadata)

        print ':: Segmentando nubes %s ::' % (datetime.datetime.utcnow())
        np_rgb, np_nubes = nubes.obtenerNubes(bandas)
        self.imagen_nubes = PIL.Image.fromarray(np_nubes.astype('uint64'))
        self.imagen_rgb = PIL.Image.fromarray(np_rgb.astype('uint64'))

        print ':: Detectando erosión %s ::' % (datetime.datetime.utcnow())
        np_ndvi, np_erosion = deteccion.detectarErosion(bandas, metadata, np_nubes)
        self.imagen_ndvi = PIL.Image.fromarray(np_ndvi.astype('uint8'))
        self.imagen_erosion = PIL.Image.fromarray(np_erosion.astype('uint8'))

        figure = plt.figure()

        ax1 = figure.add_subplot(221)
        figure.suptitle('RGB')
        ax1.imshow(np_rgb, cmap="gist_earth", interpolation='nearest')
        ax1.axis('off')
        ax2 = figure.add_subplot(222)
        figure.suptitle('Nubes')
        ax2.imshow(np_nubes, cmap='gray', interpolation='nearest')
        ax2.axis('off')
        ax3 = figure.add_subplot(223)
        figure.suptitle('Nivel Vegetacion')
        ax3.imshow(np_ndvi, cmap='RdYlGn', interpolation='nearest')
        ax3.axis('off')
        ax4 = figure.add_subplot(224)
        figure.suptitle('Erosion')
        ax4.imshow(np_erosion, cmap='gray', interpolation='nearest')
        ax4.axis('off')


        plt.axis('off')
        plt.show()

    def descargar(self):
        print ':: Descargando imágenes %s ::' % (datetime.datetime.utcnow())
        scipy.misc.imsave('%s/rgb.tif' % (self.ruta.get()),self.imagen_rgb)
        scipy.misc.imsave('%s/nubes.tif' % (self.ruta.get()),self.imagen_nubes)
        scipy.misc.imsave('%s/ndvi.tif' % (self.ruta.get()),self.imagen_ndvi)
        scipy.misc.imsave('%s/erosion.tif' % (self.ruta.get()),self.imagen_erosion)
