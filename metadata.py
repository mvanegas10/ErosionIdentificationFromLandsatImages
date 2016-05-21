#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import sys, os, math
from skimage import io, filters
from skimage.color.adapt_rgb import adapt_rgb, each_channel, hsv_value
import matplotlib.pyplot as plt
import numpy as np

# Variables globales

bandas = {}
bandas['rutas'] = {}
bandas['imagenes'] = {}
metadata = {}

# Recupera la ruta del 
def darArchivo():
    path = raw_input('Por favor ingrese la ruta de la carpeta con las imágenes y la metadata:')
    for root, dirs, files in os.walk(path):
        for archivo in files:
            if 'B1' in archivo:
                bandas[rutas]['B1'] = '%s/%s' % (root,archivo)
            elif 'B2' in archivo:
                bandas[rutas]['B2'] = '%s/%s' % (root,archivo)
            elif 'B3' in archivo:
                bandas[rutas]['B3'] = '%s/%s' % (root,archivo)
            elif 'B4' in archivo:
                bandas[rutas]['B4'] = '%s/%s' % (root,archivo)
            elif 'B5' in archivo:
                bandas[rutas]['B5'] = '%s/%s' % (root,archivo)
            elif 'B6' in archivo:
                bandas[rutas]['B6'] = '%s/%s' % (root,archivo)
            elif 'B7' in archivo:
                bandas[rutas]['B7'] = '%s/%s' % (root,archivo)
            elif 'B8' in archivo:
                bandas[rutas]['B8'] = '%s/%s' % (root,archivo)
            elif 'B9' in archivo:
                bandas[rutas]['B9'] = '%s/%s' % (root,archivo)
            elif 'B10' in archivo:
                bandas[rutas]['B10'] = '%s/%s' % (root,archivo)
            elif 'B11' in archivo:
                bandas[rutas]['B11'] = '%s/%s' % (root,archivo)
            elif 'BQA' in archivo:
                bandas[rutas]['BQA'] = '%s/%s' % (root,archivo)
            elif 'MTL' in archivo:
                metadata['ruta'] = '%s/%s' % (root,archivo)

        print bandas
    #
    # metadata = open(f,'r')
    # obtenerDatos(datos, metadata)
    # return metadata

def obtenerDatos(datos, metadata):
    linea = metadata.readline()
    while linea != '':
        if REFLECTANCE_MULT_BAND in linea:
            datos[REFLECTANCE_MULT_BAND].append('Banda%s: %s' % (linea[26:27],linea[30:]))

        if REFLECTANCE_ADD_BAND in linea:
            datos[REFLECTANCE_ADD_BAND].append('Banda%s: %s' % (linea[25:26],linea[29:]))

        if SUN_ELEVATION == linea:
            datos[SUN_ELEVATION] = linea[21:]

        linea = metadata.readline()

def obtenerBandas():
    # ruta_banda4 = raw_input('Por favor ingrese la ruta de la banda 4 (LANDSAT 8):')
    banda4 = io.imread(ruta_banda4)

    # ruta_banda5 = raw_input('Por favor ingrese la ruta de la banda 5 (LANDSAT 8):')
    banda5 = io.imread(ruta_banda5)

    atm_banda4 = (0.00002* banda4 -0.1)/ math.sin(48.95449655* math.pi/180)

    atm_banda5 = (0.00002* banda5 -0.1)/ math.sin(48.95449655* math.pi/180)

    ndvi = (atm_banda5 - atm_banda4) / (atm_banda5 + atm_banda4)

    img_min = np.min(ndvi)
    img_max = np.min(ndvi)

    # ndvi = ndvi - img_min

    new_max = img_max -img_min

    # ndvi = (ndvi * new_max)/img_max

    # plt.figure(figsize=(4, 4))
    # plt.imshow(ndvi, cmap='gray', interpolation='nearest')
    # plt.axis('off')
    # plt.show()

def obtenerNubes():

    banda4 = io.imread(ruta_banda4)
    banda3 = io.imread(ruta_banda3)
    banda2 = io.imread(ruta_banda2)
    rgb = banda4
    for i in range(len(banda4)):
        j = 0
        seguir = True
        while seguir:
            try:
                rgb[i,j] = [banda4[i,j], banda3[i,j], banda2[i,j]]
                j += 1
            except:
                j = 0
                seguir = False
    nubes = rgb
    maxi = np.max(rgb)
    maxi = maxi - (maxi//1.4)
    for i in range(len(rgb)):
        j = 0
        seguir = True
        while seguir:
            try:
                if rgb[i,j] > maxi:
                    nubes[i,j] = 1
                else:
                    nubes[i,j] = 0
                j += 1
            except:
                j = 0
                seguir = False

    # return nubes
    plt.figure(figsize=(4, 4))
    plt.imshow(nubes,cmap='gray',interpolation='nearest')
    plt.axis('off')
    plt.show()

# main
if __name__ == "__main__":
    try:
        darArchivo()
        # metadata = darArchivo()
        # obtenerBandas()
        # obtenerNubes()

    except IOError:
        print 'Por favor, ingrese una ruta válida.'
        sys.exit(0)

    # except:
    #     print 'El archivo no tiene la características de un archivo de metadata.'
    #     sys.exit(0)
