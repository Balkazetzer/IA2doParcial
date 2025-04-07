def dfs_limitado(graph, start, goal, limit):
    stack = [(start, 0)]  
    visited = set()

    while stack:
        node, depth = stack.pop()
        if node in visited or depth > limit:
            continue
        visited.add(node)
        print(f"Visitando: {node}, Profundidad: {depth}")

        if node == goal:
            print("Objetivo encontrado")
            return

        for neighbor in reversed(graph.get(node, [])):  
            stack.append((neighbor, depth + 1))

def dfs_iterativo(graph, start, goal, max_depth):
    for limit in range(max_depth + 1):
        print(f"Intentando con profundidad límite: {limit}")
        dfs_limitado(graph, start, goal, limit)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dfs_iterativo(graph, 'A', 'F', 3)
