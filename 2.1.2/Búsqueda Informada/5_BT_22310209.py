import random

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))

def tabu_search(graph, start, goal, max_iterations, tabu_size):
    current = start
    tabu_list = []
    for _ in range(max_iterations):
        print(f"Visitando: {current}")
        if current == goal:
            print("Objetivo encontrado")
            return
        neighbors = [n for n in graph.get(current, []) if n not in tabu_list]
        if not neighbors:
            print("No hay mejoras posibles, terminando búsqueda")
            return
        next_node = min(neighbors, key=lambda n: heuristic(n, goal))
        tabu_list.append(current)
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
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

tabu_search(graph, 'A', 'F', max_iterations=10, tabu_size=3)