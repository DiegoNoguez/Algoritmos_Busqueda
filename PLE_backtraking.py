def backtraking(variables, rango_variables, optimo, profundidad):
    min_val = rango_variables[profundidad][0]
    max_val = rango_variables[profundidad][1]

    # Iteramos sobre el rango (sumamos 1 para incluir el límite superior)
    for v in range(min_val, max_val + 1):
        variables[profundidad] = v
        
        # 1. Verificamos si la asignación actual es válida
        if es_completable(variables):
            
            # 2. Si no es la última variable, seguimos profundizando
            if profundidad < len(variables) - 1:
                optimo = backtraking(variables[:], rango_variables, optimo, profundidad + 1)
            else:
                # 3. Si es una hoja, evaluamos si es mejor que lo que ya tenemos
                if evalua_solucion(variables) > evalua_solucion(optimo):
                    optimo = tuple(variables) # Guardamos una copia de los valores actuales 
            
    return optimo 

def evalua_solucion(variables):
    x1, x2 = variables[0], variables[1]
    # Función objetivo: 6*x1 + 4*x2
    return 6 * x1 + 4 * x2

def es_completable(variables):
    x1, x2 = variables[0], variables[1]
    # Restricciones
    val1 = 7*x1 + 4*x2
    val2 = 6*x1 + 5*x2
    return val1 <= 150 and val2 <= 160

if __name__ == "__main__":
    variables = [0, 0]
    rango_variables = [(0, 51), (0, 76)]
    optimo = (0, 0)
    
    sol = backtraking(variables[:], rango_variables, optimo, 0)

    print("Mejor solución encontrada:")
    print(f"{sol[0]} Pantalones")
    print(f"{sol[1]} Camisetas")
    print(f"Beneficio: {evalua_solucion(sol)}")