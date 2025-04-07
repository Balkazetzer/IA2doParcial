def busqueda_online(estado_inicial, objetivo, accion, pasos_maximos=1000):
    frontera = [estado_inicial]
    visitados = set()
    while frontera:
        estado_actual = frontera.pop()
        if estado_actual == objetivo:
            return True
        if estado_actual not in visitados:
            visitados.add(estado_actual)
            if len(frontera) < pasos_maximos:
                frontera.extend(accion(estado_actual))
    return False

# Definir las acciones en el problema (ejemplo simple)
def acciones(estado):
    return [estado + 1, estado - 1]

# Uso de la búsqueda online
estado_inicial = 0
objetivo = 10
resultado = busqueda_online(estado_inicial, objetivo, acciones)
print(f"Objetivo alcanzado: {resultado}")
