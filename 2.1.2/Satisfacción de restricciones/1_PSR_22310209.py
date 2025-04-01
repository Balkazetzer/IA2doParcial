def es_valido(estado, restricciones):
    for restriccion in restricciones:
        if not restriccion(estado):
            return False
    return True

def backtracking(estado, restricciones, variables, dominio):
    if len(estado) == len(variables):
        return estado
    var = variables[len(estado)]
    for valor in dominio[var]:
        nuevo_estado = estado.copy()
        nuevo_estado[var] = valor
        if es_valido(nuevo_estado, restricciones):
            solucion = backtracking(nuevo_estado, restricciones, variables, dominio)
            if solucion:
                return solucion
    return None

# Definir el dominio y restricciones
variables = ['x', 'y', 'z']
dominio = {'x': [1, 2], 'y': [1, 2], 'z': [1, 2]}
restricciones = [
    lambda estado: estado.get('x', 0) + estado.get('y', 0) != 3,
    lambda estado: estado.get('y', 0) != estado.get('z', 0)
]

# Uso del algoritmo de backtracking
solucion = backtracking({}, restricciones, variables, dominio)
print(f"Solución: {solucion}")
