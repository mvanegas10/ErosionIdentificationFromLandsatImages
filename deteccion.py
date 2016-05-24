#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

import math
import numpy as np

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

    # Se lleva a cabo la corrección atomosférica para las bandas 2,5 y 6

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

    maxiRojo = np.max(rojo)
    maxNubes = np.max(nubes)

    # No se tienen en cuenta las nubes
    for i in range(len(rojo)):
        j = 0
        seguir = True
        while seguir:
            try:
                if nubes[i,j] == maxNubes:
                    ndvi[i,j] = maxiRojo
                else:
                    ndvi[i,j] = [rojo[i,j],verde[i,j],azul[i,j]]
                j += 1
            except:
                j = 0
                seguir = False

    maxi = np.max(ndvi)

    binary = ndvi <= (maxi - maxi*0.80)
    return ndvi, binary
