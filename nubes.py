#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np

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
    return nubes
