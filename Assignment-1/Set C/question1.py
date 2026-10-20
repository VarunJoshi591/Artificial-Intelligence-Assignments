#Write a program to solve the Water Jug Problem (4-gallon and 3-gallon jugs, goal is 2 
#gallons in the 4-gallon jug). Use an appropriate search strategy (e.g., BFS). Print the 
#sequence of states that lead to the goal.


from collections import deque

def water_jug():
    capacity4 = 4
    capacity3 = 3

    start = (0, 0)
    goal = 2

    queue = deque([start])
    visited = {start}
    parent = {start: None}

    while queue:
        a, b = queue.popleft()

        if a == goal:
            path = []
            state = (a, b)

            while state is not None:
                path.append(state)
                state = parent[state]

            path.reverse()
            return path

        # Fill the 4-gallon jug
        states = [
            (capacity4, b),
            (a, capacity3),

            # Empty the 4-gallon jug
            (0, b),

            # Empty the 3-gallon jug
            (a, 0),

            # Pour water from the 3-gallon jug into the 4-gallon jug
            (min(capacity4, a + b), max(0, b - (capacity4 - a))),

            # Pour water from the 4-gallon jug into the 3-gallon jug
            (max(0, a - (capacity3 - b)), min(capacity3, a + b))
        ]

        for next_state in states:
            if next_state not in visited:
                visited.add(next_state)
                parent[next_state] = (a, b)
                queue.append(next_state)

    return None


path = water_jug()

if path:
    print("Sequence of states:")
    for state in path:
        print(state)

    print("Goal reached:", path[-1])
else:
    print("No solution found.")
