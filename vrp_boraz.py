# Algoritmo de VRP Boraz 

import math 
from operator import itemgetter

def distancia(coord1, coord2):
    lon = coord1[0]
    lon2 = coord2[1]
    lat1 = coord1[0]
    lat2 = coord2[1]
    return math.sqrt((lat1-lat2)**2 +(lon-lon2)**2)

def en_ruta(rutas, c):
    ruta = None
    for r in rutas:
        if c in r:
            ruta = r
    return ruta

def peso_ruta(ruta):
    total = 0
    for c in ruta:
        total = total + pedidos[c]
    return total

def vrp_voraz():
    #Calculo de los ahorros
    s = ()
    for c1 in coord:
        for c2 in coord:
            if c1 != c2:
                if not (c2,c1) in s:
                    d_c1_c2 = distancia(coord[c1],coord[c2])
                    d_c1_almacen = distancia(coord[c1],almacen)
                    d_c2_almacen = distancia(coord[c2], almacen)
                    s[c1,c2] = d_c1_almacen + d_c2_almacen - d_c1_c2
        # ordenar ahorros 
        s = sorted(s.items(), key=itemgetter(1), reverse=True)

        # construir ruta 
        rutas = []
        for k,v in s:
            rc1 = en_ruta(rutas, k[0])
            rc2 = en_ruta(rutas, k[1])
            if rc1 == None and rc2 ==None:
                # no estan en ninguna ruta. Se crea 
                if peso_ruta([k[0],k[1]]) <= max_carga:
                    rutas.append([k[0],k[1]])