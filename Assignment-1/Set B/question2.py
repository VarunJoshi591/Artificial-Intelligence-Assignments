#Modify the A* code to implement the Greedy Best-First Search (where f(n)=h(n)). Compare 
#the path found and the number of nodes expanded with the A* search result.


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
    'Arad': 366, 'Zerind': 374, 'Oradea': 380,
    'Sibiu': 253, 'Timisoara': 329, 'Lugoj': 244,
    'Mehadia': 241, 'Drobeta': 242, 'Craiova': 160,
    'Rimnicu Vilcea': 193, 'Fagaras': 176,
    'Pitesti': 100, 'Bucharest': 0
}


def best_first_search(graph, start, goal, greedy):
    pq = [(heuristic[start], 0, start)]
    parent = {start: None}
    cost = {start: 0}
    expanded = 0

    while pq:
        f, g, current = heapq.heappop(pq)

        if g != cost[current]:
            continue

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g, expanded

        expanded += 1

        for neighbour, distance in graph[current].items():
            new_cost = g + distance

            if neighbour not in cost or new_cost < cost[neighbour]:
                cost[neighbour] = new_cost
                parent[neighbour] = current

                if greedy:
                    priority = heuristic[neighbour]
                else:
                    priority = new_cost + heuristic[neighbour]

                heapq.heappush(
                    pq, (priority, new_cost, neighbour)
                )

    return [], None, expanded


start = 'Arad'
goal = 'Bucharest'

# A* Search
astar_path, astar_cost, astar_expanded = best_first_search(
    graph, start, goal, False
)

# Greedy Best-First Search
greedy_path, greedy_cost, greedy_expanded = best_first_search(
    graph, start, goal, True
)

print("A* Search Path:", " -> ".join(astar_path))
print("A* Total Cost:", astar_cost, "km")
print("A* Nodes Expanded:", astar_expanded)

print("\nGreedy Best-First Search Path:",
      " -> ".join(greedy_path))
print("Greedy Total Cost:", greedy_cost, "km")
print("Greedy Nodes Expanded:", greedy_expanded)
