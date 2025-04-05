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
    'Chennai': {'Dubai': 500, 'Mumbai': 450 , 'Doha': 600},
    'Dubai': {'London': 700, 'Frankfort': 650},
    'Mumbai': {'Frankfort': 620},
    'Doha': {'Paris' : 680},
    'London': {'Boston' : 400},
    'Frankfort': {'Toronto': 500},
    'Paris': {'Toronto': 450},
    'Boston': {'NewYork': 200},
    'Toronto': {'NewYork': 300},
    'NewYork': {}
}


heuristic = {
    'Chennai': 12,
    'Dubai': 7.5,  
    'Mumbai': 7,   
    'Doha': 5,
    'London': 8,
    'Frankfort': 7,
    'Paris': 2.5,
    'Boston': 7,   
    'Toronto': 6,
    'NewYork': 2, 
}

start = 'Chennai'  
goal = 'NewYork'  

path = a_star_search(graph, start, goal, heuristic)
print(f"Path: {path}")
