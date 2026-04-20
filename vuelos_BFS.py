# Vuelos con Busqueda en amplitud. 
from arbol import Nodo 

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados=[]
    nodos_frontera=[]
    nodo_inicial= Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) !=0:
        nodo=nodos_frontera[0]

        # Extracción de nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos()==solucion:
            # Solucion encontrada
            solucionado = True
            return nodo 
        else:
            # Expandir nodos hijos (Ciudades con conexión). 
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                lista_hijos.append(hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)
        nodo.set_hijos(lista_hijos)

if __name__ == "__main__":
    conexiones = {
        'JILOYORK': {'CELAYA', 'CDMX','QUERÉTARO'},
        'SONORA': {'ZACATECAS', 'SINALOA'},
        'GUANAJUATO': {'AGUASCALIENTES'},
        'OAXACA': {'QUERÉTARO'},
        'SINALOA': {'CELAYA', 'SONORA', 'JILOYORK'},
        'CDMX': {'MONTERREY'},
        'CELAYA': {'JILOYORK', 'SINALOA'},
        'ZACATECAS': {'SONORA', 'MONTERREY', 'QUERÉTARO'},
        'MONTERREY': {'ZACATECAS','MONTERREY'},
        'TAMAULIPAS': {'QUERÉTARO'},
        'QUERÉTARO': {'TAMAULIPAS', 'ZACATECAS', 'SINALOA', 'JILOYORK', 'OAXACA'}
    }

    estado_inicial = 'JILOYORK'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    # Mostrar el resultado de solución 
    resultado = []
    nodo = nodo_solucion

    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print (f'{resultado}')
    


