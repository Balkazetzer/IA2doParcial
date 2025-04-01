def busqueda_en_grafos(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)

        print(f"Visitando: {node}")

        if node == goal:
            print("Camino encontrado:", " -> ".join(path))
            return path
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

busqueda_en_grafos(graph, 'A', 'F')
