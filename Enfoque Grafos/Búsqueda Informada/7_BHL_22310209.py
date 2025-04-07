import random

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))

def local_beam_search(graph, start, goal, k):
    states = [start] * k  # Inicializa k estados con el nodo inicial
    while True:
        print(f"Estados actuales: {states}")
        if goal in states:
            print("Objetivo encontrado")
            return
        all_neighbors = []
        for state in states:
            all_neighbors.extend(graph.get(state, []))
        if not all_neighbors:
            print("No hay mejoras posibles, terminando búsqueda")
            return
        states = sorted(all_neighbors, key=lambda n: heuristic(n, goal))[:k]

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

local_beam_search(graph, 'A', 'F', k=2)