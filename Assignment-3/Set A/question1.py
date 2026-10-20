# Implement the Minimax algorithm (with a fixed depth limit) for a given game tree (or
#a simple game like Nim). Assume the initial player is the MAX player. Display the 
#optimal move and the resulting utility value

# Minimax Algorithm with Fixed Depth Limit

# Game tree represented as a dictionary
game_tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

# Utility values of leaf nodes
utility = {
    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}

# Minimax algorithm
def minimax(node, depth, maximizing_player):

    # Stop at leaf node or depth limit
    if depth == 0 or not game_tree[node]:
        return utility.get(node, 0)

    if maximizing_player:
        best_value = float("-inf")

        for child in game_tree[node]:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)

        return best_value

    else:
        best_value = float("inf")

        for child in game_tree[node]:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)

        return best_value


# Find the optimal move for MAX
best_move = None
best_value = float("-inf")

for child in game_tree["A"]:
    value = minimax(child, 2, False)

    print("Move to", child, "gives utility:", value)

    if value > best_value:
        best_value = value
        best_move = child

print("\nOptimal move for MAX:", best_move)
print("Resulting utility value:", best_value)
