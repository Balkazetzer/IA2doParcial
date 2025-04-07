import random

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))

def hill_climbing(graph, start, goal):
    current = start
    while True:
        print(f"Visitando: {current}")
        if current == goal:
            print("Objetivo encontrado")
            return
        neighbors = graph.get(current, [])
        if not neighbors:
            print("No hay mejoras posibles, terminando búsqueda")
            return
        next_node = min(neighbors, key=lambda n: heuristic(n, goal))
        if heuristic(next_node, goal) >= heuristic(current, goal):
            print("No hay mejoras posibles, terminando búsqueda")
            return
        current = next_node

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

hill_climbing(graph, 'A', 'F')