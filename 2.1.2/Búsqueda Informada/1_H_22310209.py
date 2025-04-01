import heapq

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))  # Diferencia entre caracteres como heurística

def best_first_search(graph, start, goal):
    priority_queue = [(heuristic(start, goal), start)]
    visited = set()

    while priority_queue:
        _, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        print(f"Visitando: {node}")

        if node == goal:
            print("Objetivo encontrado")
            return

        for neighbor in graph.get(node, []):
            heapq.heappush(priority_queue, (heuristic(neighbor, goal), neighbor))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

best_first_search(graph, 'A', 'F')
