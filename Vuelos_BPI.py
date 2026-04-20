# Algorito de busqueda en profundidad de manera iteractiva en el problema de los vuelos

from arbol import Nodo

def DFS_prof_iter(nodo, solucion):
    for limite in range(0,100):
        visitados=[]
        sol = buscar_solucion_DFS_Rec(nodo, solucion, visitados, limite)
        if sol!=None:
            return sol
        
def buscar_solucion_DFS_Rec(nodo, solcuion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solcuion:
            return nodo 
        else:
            # Se expandira el árbol 
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
            
            nodo.set_hijos(lista_hijos)

            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    # Recursividad del algoritmo 
                    sol = buscar_solucion_DFS_Rec(nodo_hijo, solcuion, visitados, limite-1)
                    if sol !=None:
                        return sol
    
    return None

if __name__  == "__main__":
    conexiones ={
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
    solucion = 'OAXACA'
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_prof_iter(nodo_inicial, solucion)

    if nodo != None:
        resultado = []
        while nodo.get_padre() !=None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print (resultado)
    else:
        print(f'Resultado no encontrado')