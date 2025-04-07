import heapq

def heuristic(node, goal):
    return abs(ord(goal) - ord(node))  # Diferencia entre caracteres como heurística

def a_star(graph, start, goal, cost):
    open_list = [(0, start)]
    g_score = {start: 0}
    while open_list:
        _, node = heapq.heappop(open_list)
        if node == goal:
            print("Objetivo encontrado")
            return
        for neighbor in graph.get(node, []):
            temp_g = g_score[node] + cost[node][neighbor]
            if neighbor not in g_score or temp_g < g_score[neighbor]:
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

def ao_star(graph, start, goal, cost):
    open_list = [(heuristic(start, goal), start)]
    solution = {}
    while open_list:
        _, node = heapq.heappop(open_list)
        if node == goal:
            print("Objetivo encontrado")
            return
        best_cost = float('inf')
        best_path = None
        for neighbor in graph.get(node, []):
            path_cost = cost[node][neighbor] + heuristic(neighbor, goal)
            if path_cost < best_cost:
                best_cost = path_cost
                best_path = neighbor
        if best_path:
            solution[node] = best_path
            heapq.heappush(open_list, (best_cost, best_path))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

cost = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 1, 'E': 2},
    'C': {'F': 3, 'G': 5},
    'D': {},
    'E': {},
    'F': {},
    'G': {}
}

a_star(graph, 'A', 'F', cost)
ao_star(graph, 'A', 'F', cost)
