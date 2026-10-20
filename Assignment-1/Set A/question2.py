#Write a program to implement Breadth-First Search (BFS) for a given graph. Use an 
#adjacency list representation for the graph. Print the traversal order and the shortest path from a 
#source node to a destination node


from collections import deque

# Graph represented using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    traversal = []

    while queue:
        node = queue.popleft()
        traversal.append(node)

        if node == goal:
            break

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = node
                queue.append(neighbour)

    # Reconstruct the shortest path
    path = []

    if goal in visited:
        current = goal

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()

    return traversal, path


start = 'A'
goal = 'F'

traversal, path = bfs(graph, start, goal)

print("BFS Traversal:", traversal)

if path:
    print("Shortest Path:", " -> ".join(path))
else:
    print("No path exists between", start, "and", goal)

