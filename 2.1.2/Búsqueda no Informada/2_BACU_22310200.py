import heapq

def ucs(graph, start, goal):
    priority_queue = [(0, start)]  # (costo, nodo)
    visited = set()

    while priority_queue:
        cost, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        print(f"Visitando: {node} con costo: {cost}")

        if node == goal:
            print("Objetivo encontrado con costo mínimo:", cost)
            return
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor))

# Grafo con costos
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5)],
    'F': [('C', 3)]
}

ucs(graph, 'A', 'F')

