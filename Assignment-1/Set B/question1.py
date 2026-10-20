# Implement the A* search algorithm to find the shortest path from a starting city to a goal city 
#on a simplified map (e.g., Romania map). Use the straight-line distance to the goal as the 
#heuristic function h(n). Display the search path and total path cost.


import heapq

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151,
              'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146,
                'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146,
                       'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138,
                'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}


heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0
}

def a_star(graph, start, goal):
    priority_queue = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if g != cost[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g

        for neighbour, distance in graph[current].items():
            new_cost = g + distance

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current

                f_cost = new_cost + heuristic[neighbour]
                heapq.heappush(
                    priority_queue,
                    (f_cost, new_cost, neighbour)
                )

    return [], None


start = 'Arad'
goal = 'Bucharest'

path, total_cost = a_star(graph, start, goal)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Path Cost:", total_cost, "km")
else:
    print("No path found.")
