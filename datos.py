#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Obtiene los datos de la metadata
def obtenerDatos(metadata):
    archivo = open(metadata['ruta'],'r')
    linea = archivo.readline()
    while linea != '':
        datos = linea.split("=")
        for i in range(len(datos)):
            datos[i] = datos[i].strip()
        if len(datos) == 2:
            metadata[datos[0]] = datos[1]
        linea = archivo.readline()
