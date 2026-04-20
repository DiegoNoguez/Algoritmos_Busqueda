# Algoritmo de busqueda en profundidad BFS con recursividad y diseñado para detenerse en limite y evitar un ciclo infinito 
from arbol import Nodo

def buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados, limite):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    
    # Se alcanzó el límite de profundidad
    elif limite == 0:
        return "corte_limite"
    
    else:
        # Variable para rastrear si algún hijo quedó truncado por el límite
        hubo_corte = False
        # Expandir nodos sucesores
        dato_nodo = nodo_inicial.get_datos()
        
        hijo_izq_datos = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo_izq_datos)
        hijo_izquierdo.set_padre(nodo_inicial) # Importante para reconstruir el camino

        hijo_cen_datos = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo_cen_datos)
        hijo_central.set_padre(nodo_inicial)

        hijo_der_datos = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo_der_datos)
        hijo_derecho.set_padre(nodo_inicial)

        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                # LLAMADA RECURSIVA: Pasamos límite - 1
                sol = buscar_solucion_DFS_Rec(nodo_hijo, solucion, visitados, limite - 1)
                
                if sol == "corte_limite":
                    hubo_corte = True
                elif sol is not None:
                    return sol
        
        # Si no encontramos la solución pero algún hijo fue cortado
        return "corte_limite" if hubo_corte else None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    limite_maximo = 10 # Definimos un límite el limite de momento es de 10 
    
    nodo_inicial = Nodo(estado_inicial)
    # Pasamos el límite a la función y uso de la recursividad 
    nodo_solucion = buscar_solucion_DFS_Rec(nodo_inicial, solucion, visitados, limite_maximo)

    # Ipresion de los resultados en caso de haber o no haber debido al limite definido
    # Mostrar resultados
    if nodo_solucion == "corte_limite":
        print("No se encontró solución dentro del límite de profundidad.")
    elif nodo_solucion is None:
        print("No existe solución en este espacio de estados.")
    else:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(f"{resultado}")