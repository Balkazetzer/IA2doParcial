import math
import random

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))

def simulated_annealing(graph, start, goal, initial_temp, cooling_rate):
    current = start
    temperature = initial_temp
    while temperature > 1:
        print(f"Visitando: {current}, Temperatura: {temperature:.2f}")
        if current == goal:
            print("Objetivo encontrado")
            return
        neighbors = graph.get(current, [])
        if not neighbors:
            print("No hay más opciones, terminando búsqueda")
            return
        next_node = random.choice(neighbors)
        delta_e = heuristic(current, goal) - heuristic(next_node, goal)
        if delta_e > 0 or math.exp(delta_e / temperature) > random.random():
            current = next_node
        temperature *= cooling_rate

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

simulated_annealing(graph, 'A', 'F', initial_temp=100, cooling_rate=0.9) 