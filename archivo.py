#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from skimage import io

# Recupera la ruta de las imágenes y la metadata
def darArchivo(bandas, metadata, path):
    for root, dirs, files in os.walk(path):
        for archivo in files:
            if 'B1' in archivo:
                bandas['rutas']['B1'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B1'] = io.imread(bandas['rutas']['B1'])
            elif 'B2' in archivo:
                bandas['rutas']['B2'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B2'] = io.imread(bandas['rutas']['B2'])
            elif 'B3' in archivo:
                bandas['rutas']['B3'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B3'] = io.imread(bandas['rutas']['B3'])
            elif 'B4' in archivo:
                bandas['rutas']['B4'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B4'] = io.imread(bandas['rutas']['B4'])
            elif 'B5' in archivo:
                bandas['rutas']['B5'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B5'] = io.imread(bandas['rutas']['B5'])
            elif 'B6' in archivo:
                bandas['rutas']['B6'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B6'] = io.imread(bandas['rutas']['B6'])
            elif 'B7' in archivo:
                bandas['rutas']['B7'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B7'] = io.imread(bandas['rutas']['B7'])
            elif 'B8' in archivo:
                bandas['rutas']['B8'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B8'] = io.imread(bandas['rutas']['B8'])
            elif 'B9' in archivo:
                bandas['rutas']['B9'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B9'] = io.imread(bandas['rutas']['B9'])
            elif 'B10' in archivo:
                bandas['rutas']['B10'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B10'] = io.imread(bandas['rutas']['B10'])
            elif 'B11' in archivo:
                bandas['rutas']['B11'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['B11'] = io.imread(bandas['rutas']['B11'])
            elif 'BQA' in archivo:
                bandas['rutas']['BQA'] = '%s/%s' % (root,archivo)
                bandas['imagenes']['BQA'] = io.imread(bandas['rutas']['BQA'])
            elif 'MTL' in archivo:
                metadata['ruta'] = '%s/%s' % (root,archivo)
