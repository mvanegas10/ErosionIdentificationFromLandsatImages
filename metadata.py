#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
REFLECTANCE_MULT_BAND = 'REFLECTANCE_MULT_BAND'
REFLECTANCE_ADD_BAND = 'REFLECTANCE_ADD_BAND'
SUN_ELEVATION = 'SUN_ELEVATION'

def darArchivo():
    f = raw_input('Por favor ingrese la ruta del archivo de metadata:')
    metadata = open(f,'r')
    return metadata

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

# main
if __name__ == "__main__":
    datos = {};
    datos[REFLECTANCE_MULT_BAND] = []
    datos[REFLECTANCE_ADD_BAND] = []
    datos[SUN_ELEVATION] = 0.0
    try:
        metadata = darArchivo()
        obtenerDatos(datos, metadata)
        print 'Los datos son los siguientes:'
        print datos

    except IOError:
        print 'La ruta no es válida.'
        sys.exit(0)

    except:
        print 'El archivo no tiene la características de un archivo de metadata.'
        sys.exit(0)
