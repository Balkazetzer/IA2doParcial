from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node in visited:
            continue
        visited.add(node)
        print(f"Visitando: {node}")

        if node == goal:
            print("Objetivo encontrado")
            return
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)

# Ejemplo de grafo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

bfs(graph, 'A', 'F')

