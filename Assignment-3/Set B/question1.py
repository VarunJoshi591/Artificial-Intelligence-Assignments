# Implement the Alpha-Beta Pruning algorithm on the same game tree used in 3.1. 
# Display the nodes that were pruned and compare the performance (number of nodes 
# visited) with the Minimax algorithm.


# Alpha-Beta Pruning Algorithm

game_tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

utility = {
    "D": 3,
    "E": 5,
    "F": 2,
    "G": 9
}

# Minimax algorithm with node counting
minimax_count = 0

def minimax(node, maximizing_player):
    global minimax_count
    minimax_count += 1

    if not game_tree[node]:
        return utility[node]

    if maximizing_player:
        best_value = float("-inf")
        for child in game_tree[node]:
            value = minimax(child, False)
            best_value = max(best_value, value)
        return best_value

    else:
        best_value = float("inf")
        for child in game_tree[node]:
            value = minimax(child, True)
            best_value = min(best_value, value)
        return best_value


# Alpha-Beta Pruning algorithm
alpha_beta_count = 0
pruned_nodes = []

def alpha_beta(node, alpha, beta, maximizing_player):
    global alpha_beta_count
    alpha_beta_count += 1

    if not game_tree[node]:
        return utility[node]

    if maximizing_player:
        best_value = float("-inf")

        for i, child in enumerate(game_tree[node]):
            value = alpha_beta(child, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                pruned_nodes.extend(game_tree[node][i + 1:])
                print("Pruned nodes:", game_tree[node][i + 1:])
                break

        return best_value

    else:
        best_value = float("inf")

        for i, child in enumerate(game_tree[node]):
            value = alpha_beta(child, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                pruned_nodes.extend(game_tree[node][i + 1:])
                print("Pruned nodes:", game_tree[node][i + 1:])
                break

        return best_value


# Run Minimax
print("----- Minimax -----")
minimax_value = minimax("A", True)
print("Optimal utility:", minimax_value)
print("Nodes visited:", minimax_count)

# Run Alpha-Beta Pruning
print("\n----- Alpha-Beta Pruning -----")
alpha_beta_value = alpha_beta(
    "A", float("-inf"), float("inf"), True
)
print("Optimal utility:", alpha_beta_value)
print("Nodes visited:", alpha_beta_count)
print("All pruned nodes:", pruned_nodes)


