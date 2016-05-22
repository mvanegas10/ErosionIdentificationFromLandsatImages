#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# Segmenta las nubes
def obtenerNubes(bandas):
    rojo = bandas['imagenes']['B4']
    verde = bandas['imagenes']['B3']
    azul = bandas['imagenes']['B2']
    rgb = rojo

    for i in range(len(rojo)):
        j = 0
        seguir = True
        while seguir:
            try:
                rgb[i,j] = [rojo[i,j], verde[i,j], azul[i,j]]
                j += 1
            except:
                j = 0
                seguir = False
    maxi = np.max(rgb)
    maxi = maxi - (maxi/1.4)
    nubes = rgb > maxi
    nubes2 = nubes
    rgb = np.multiply(rgb,20)
    return rgb, nubes
