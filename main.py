#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, datetime
import archivo, datos, nubes, deteccion

# main
if __name__ == "__main__":

    # Variables globales
    bandas = {}
    bandas['rutas'] = {}
    bandas['imagenes'] = {}
    metadata = {}

    try:
        archivo.darArchivo(bandas, metadata)
        print ':: Obteniendo datos %s ::' % (datetime.datetime.utcnow())
        datos.obtenerDatos(metadata)
        print ':: Segmentando nubes %s ::' % (datetime.datetime.utcnow())
        nubes = nubes.obtenerNubes(bandas)
        print ':: Detectando erosión %s ::' % (datetime.datetime.utcnow())
        deteccion.detectarErosion(bandas, metadata, nubes)

    except IOError:
        print 'Por favor, ingrese una ruta válida.'
        sys.exit(0)
