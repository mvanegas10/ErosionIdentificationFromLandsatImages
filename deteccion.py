#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import threshold_otsu

def detectarErosion(bandas, metadata, nubes):
    IRCercano = bandas['imagenes']['B5']
    rojo = bandas['imagenes']['B4']

    mpIRCercano = float(metadata['REFLECTANCE_MULT_BAND_5'])
    mpRojo = float(metadata['REFLECTANCE_MULT_BAND_4'])

    apIRCercano = float(metadata['REFLECTANCE_ADD_BAND_5'])
    apRojo = float(metadata['REFLECTANCE_ADD_BAND_5'])

    se = float(metadata['SUN_ELEVATION'])
    sin_se = math.sin( se * math.pi/180 )

    # Se lleva a cabo la corrección atomosférica para las bandas del infrarojo cercano y el rojo

    correccionIRC = np.multiply(mpIRCercano,IRCercano)
    correccionIRC = np.add(correccionIRC,apIRCercano)
    correccionIRC = np.true_divide(correccionIRC,sin_se)

    correccionR = np.multiply(mpRojo,rojo)
    correccionR = np.add(correccionR,apRojo)
    correccionR = np.true_divide(correccionR,sin_se)

    # Se calcula el NDVI
    ndvi = np.divide(np.subtract(correccionIRC,correccionR),np.add(correccionIRC,correccionR),dtype=float)

    # No se tienen en cuenta las nubes
    for i in range(len(nubes)):
        j = 0
        seguir = True
        while seguir:
            try:
                if ndvi[i,j] == float('inf'):
                    ndvi[i,j] = 100
                if nubes[i,j] == 1:
                    ndvi[i,j] = 100
                j += 1
            except:
                j = 0
                seguir = False

    binary = ndvi <= 0

    plt.figure(figsize=(4, 4))
    plt.imshow(binary, cmap='gray', interpolation='nearest')
    plt.axis('off')
    plt.show()
