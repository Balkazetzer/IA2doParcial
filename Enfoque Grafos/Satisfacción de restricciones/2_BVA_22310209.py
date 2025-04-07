def es_valido(estado, restricciones):
    # Verificar si el estado actual cumple con las restricciones
    for restriccion in restricciones:
        if not restriccion(estado):
            return False
    return True

def backtracking(estado, restricciones, variables, dominio):
    # Caso base: si hemos asignado valores a todas las variables, devolvemos el estado
    if len(estado) == len(variables):
        return estado
    
    # Elegir la siguiente variable a asignar
    var = variables[len(estado)]
    
    # Probar cada valor posible en el dominio de la variable
    for valor in dominio[var]:
        nuevo_estado = estado.copy()
        nuevo_estado[var] = valor
        
        # Si la asignación es válida, hacemos la llamada recursiva
        if es_valido(nuevo_estado, restricciones):
            solucion = backtracking(nuevo_estado, restricciones, variables, dominio)
            if solucion:
                return solucion
    
    # Si no encontramos una solución, retrocedemos
    return None

# Definir el dominio y las restricciones
variables = ['x', 'y', 'z']
dominio = {'x': [1, 2], 'y': [1, 2], 'z': [1, 2]}

# Restricciones del problema
restricciones = [
    lambda estado: estado.get('x', 0) + estado.get('y', 0) != 3,  # x + y != 3
    lambda estado: estado.get('y', 0) != estado.get('z', 0)  # y != z
]

# Llamada al algoritmo de backtracking
solucion = backtracking({}, restricciones, variables, dominio)
print(f"Solución encontrada: {solucion}")
