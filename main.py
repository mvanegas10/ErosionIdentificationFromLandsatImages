#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, datetime
import archivo, datos, nubes

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
        nubes.obtenerNubes(bandas)
        print ':: Detectando erosión %s ::' % (datetime.datetime.utcnow())

    except IOError:
        print 'Por favor, ingrese una ruta válida.'
        sys.exit(0)
