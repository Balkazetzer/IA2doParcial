def bidirectional_search(graph, start, goal):
    front_start = {start}
    front_goal = {goal}
    visited_start = set()
    visited_goal = set()

    while front_start and front_goal:
        if front_start & front_goal:
            print("Camino encontrado")
            return True

        visited_start.update(front_start)
        visited_goal.update(front_goal)

        front_start = {neighbor for node in front_start for neighbor in graph.get(node, []) if neighbor not in visited_start}
        front_goal = {neighbor for node in front_goal for neighbor in graph.get(node, []) if neighbor not in visited_goal}

    print("No se encontró camino")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

bidirectional_search(graph, 'A', 'F')
