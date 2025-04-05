import heapq
from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
        self.weight = {}
        self.heuristic = {}

    def addedges(self, u, v, weight: int = 1):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.weight[(u, v)] = weight
        self.weight[(v, u)] = weight

    def set_heuristics(self, node, value):
        self.heuristic[node] = value

    def print_graph(self):
        for node, neighbors in self.graph.items():
            print(f"{node}: {', '.join(neighbors)}")

    def ucs_search(self, start, goal):
        queue = [(0, start, [start])]
        visited = set()
        while queue:
            cost, node, path = heapq.heappop(queue)
            if node == goal:
                return path
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + self.weight.get((node, neighbor), 1)
                        heapq.heappush(queue, (new_cost, neighbor, path + [neighbor]))
        return []

g = Graph()
edges = [('A', 'B', 4), ('A', 'C', 3), ('C', 'E', 10), ('C', 'D', 7), ('D', 'E', 2), 
         ('B', 'E', 12), ('B', 'F', 5), ('F', 'Z', 16), ('E', 'Z', 5)]

heuristics = {'A': 14, 'B': 12, 'C': 11, 'E': 4, 'D': 6, 'F': 11, 'Z': 0}

for edge in edges:
    g.addedges(*edge)

for node, value in heuristics.items():
    g.set_heuristics(node, value)

start, goal = 'A', 'Z'

print("The graph:\n")
g.print_graph()

print("\nThe UCS search path from {} to {}:\n".format(start, goal))
path = g.ucs_search(start, goal)
print(path)
