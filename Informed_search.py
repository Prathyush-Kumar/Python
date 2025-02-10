import heapq

def a_star_search(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic[start]

    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current].items():
            temp_g_score = g_score[current] + cost

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + heuristic[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'D': 5},
    'D': {'B': 2, 'C': 5}
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1
}

start = 'A'
goal = 'D'

path = a_star_search(graph, start, goal, heuristic)
print(f"Path: {path}")
