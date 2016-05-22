#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import math
import numpy as np
from skimage.filters import threshold_otsu

# def detectarErosion(bandas, metadata, nubes):
#     IRCercano = bandas['imagenes']['B5']
#     rojo = bandas['imagenes']['B4']
#
#     mpIRCercano = float(metadata['REFLECTANCE_MULT_BAND_5'])
#     mpRojo = float(metadata['REFLECTANCE_MULT_BAND_4'])
#
#     apIRCercano = float(metadata['REFLECTANCE_ADD_BAND_5'])
#     apRojo = float(metadata['REFLECTANCE_ADD_BAND_5'])
#
#     se = float(metadata['SUN_ELEVATION'])
#     sin_se = math.sin( se * math.pi/180 )
#
#     # Se lleva a cabo la corrección atomosférica para las bandas del infrarojo cercano y el rojo
#
#     correccionIRC = np.multiply(mpIRCercano,IRCercano)
#     correccionIRC = np.add(correccionIRC,apIRCercano)
#     correccionIRC = np.true_divide(correccionIRC,sin_se)
#
#     correccionR = np.multiply(mpRojo,rojo)
#     correccionR = np.add(correccionR,apRojo)
#     correccionR = np.true_divide(correccionR,sin_se)
#
#     # Se calcula el NDVI
#     ndvi = np.divide(np.subtract(correccionIRC,correccionR),np.add(correccionIRC,correccionR),dtype=float)
#
#     # No se tienen en cuenta las nubes
#     for i in range(len(nubes)):
#         j = 0
#         seguir = True
#         while seguir:
#             try:
#                 if ndvi[i,j] == float('inf'):
#                     ndvi[i,j] = 100
#                 if nubes[i,j] == 1:
#                     ndvi[i,j] = 100
#                 j += 1
#             except:
#                 j = 0
#                 seguir = False
#
#     binary = ndvi <= 0
#     return ndvi, binary

def detectarErosion(bandas, metadata, nubes):
    rojo = bandas['imagenes']['B5']
    verde = bandas['imagenes']['B6']
    azul = bandas['imagenes']['B2']

    mpRojo = float(metadata['REFLECTANCE_MULT_BAND_5'])
    mpVerde = float(metadata['REFLECTANCE_MULT_BAND_6'])
    mpAzul = float(metadata['REFLECTANCE_MULT_BAND_2'])

    apRojo = float(metadata['REFLECTANCE_ADD_BAND_5'])
    apVerde = float(metadata['REFLECTANCE_ADD_BAND_6'])
    apAzul = float(metadata['REFLECTANCE_ADD_BAND_2'])

    se = float(metadata['SUN_ELEVATION'])
    sin_se = math.sin( se * math.pi/180 )

    # Se lleva a cabo la corrección atomosférica para las bandas del infrarojo cercano y el rojo

    correccionR = np.multiply(mpRojo,rojo)
    correccionR = np.add(correccionR,apRojo)
    correccionR = np.true_divide(correccionR,sin_se)

    correccionV = np.multiply(mpVerde,verde)
    correccionV = np.add(correccionV,apVerde)
    correccionV = np.true_divide(correccionV,sin_se)

    correccionA = np.multiply(mpAzul,azul)
    correccionA = np.add(correccionA,apAzul)
    correccionA = np.true_divide(correccionA,sin_se)

    ndvi = rojo

    minNubes = np.min(nubes)
    maxNubes = np.max(nubes)

    # No se tienen en cuenta las nubes
    for i in range(len(rojo)):
        j = 0
        seguir = True
        while seguir:
            try:
                # if nubes[i,j] == minNubes:
                ndvi[i,j] = [rojo[i,j],verde[i,j],azul[i,j]]
                # elif nubes[i,j] == maxNubes:
                #     ndvi[i,j] = maxiI
                j += 1
            except:
                j = 0
                seguir = False

    maxi = np.max(ndvi)

    for i in range(len(ndvi)):
        j = 0
        seguir = True
        while seguir:
            try:
                if nubes[i,j] == maxNubes:
                    ndvi[i,j] = maxiI
                j += 1
            except:
                j = 0
                seguir = False


    binary = ndvi <= (maxi - maxi*0.80)
    return ndvi, binary
