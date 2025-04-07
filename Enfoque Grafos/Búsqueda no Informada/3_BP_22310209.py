def dfs(graph, start, goal):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        print(f"Visitando: {node}")

        if node == goal:
            print("Objetivo encontrado")
            return

        for neighbor in reversed(graph.get(node, [])):  
            if neighbor not in visited:
                stack.append(neighbor)

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

dfs(graph, 'A', 'F')
