# Viaje por carretera mediante coste uniforme 
from arbol import Nodo
from functools import cmp_to_key

def compara (x, y):
    return x.get_costo() - y.get_costo()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado=False
    nodos_visitados=[] 
    nodos_frontera=[] 
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)
    
    while (not solucionado) and len(nodos_frontera)!=0:
        nodos_frontera = sorted(nodos_frontera, key=lambda x: x.get_costo())
        nodo=nodos_frontera[0]
        # extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        
        if nodo.get_datos() == solucion:
            solucionado=True
            return nodo
        else:
            # expandir nodos hijo (ciudades con conexión)
            dato_nodo = nodo.get_datos()
            lista_hijos=[]
            for un_hijo in conexiones[dato_nodo]:
                hijo=Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
                hijo.set_costo(nodo.get_costo() + coste)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo()>hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                    else:
                        nodos_frontera.append(hijo)
            nodo.set_hijos(lista_hijos)

    
if __name__ == "__main__": 
    conexiones = {
        'JILOYORK':{'CDMX':125, 'QRO':513},
        'MORELOS':{'QRO':524},
        'CDMX':{'JILOYORK':125,'QRO':433, 'HGO':491},
        'HGO':{'CDMX':491, 'QRO':433, 'MEXICALI':309, 'MTY':346},
        'QRO':{'SLP':203,'MORELOS':514,'JILOYORK':513, 'CDMX':423, 'MTY':603, \
                'SONORA':437, 'HGO':356, 'MEXICALI':313, 'AGS':599},
        'SLP':{'AGS':390, 'QRO':203},
        'AGS':{'SLP':390, 'QRO':599},
        'SONORA':{'QRO':437, 'MEXICALI':394},
        'MEXICALI':{'MTY':296, 'HGO':309, 'QRO':313},
        'MTY':{'MEXICALI':296, 'QRO':603, 'HGO':3460}
    }

    estado_inicial = "JILOYORK"
    solucion = "AGS"
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    

    if nodo_solucion is not None:
        # IMpresion de la solución
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print (f'{resultado}')
        print (f'Coste: {nodo_solucion.get_costo()} KM')
    else:
        print(f'No se encontro una solución optima')