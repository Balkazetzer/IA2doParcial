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

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dfs_limitado(graph, 'A', 'F', 2)
