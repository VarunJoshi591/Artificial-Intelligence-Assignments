# Assignment 3: Adversarial Search and Game Playing

Based on Assignment 3 in the M.Sc. Computer Science AI practical lab book (Academic Year 2026–2027).

---

## Practicals Overview

| Set | File | Topic / Problem Statement | Algorithm |
|---|---|---|---|
| **Set A - Q1** | [`Set A/question1.py`](Set%20A/question1.py) | Minimax search on game tree with depth limit | Minimax Algorithm |
| **Set B - Q1** | [`Set B/question1.py`](Set%20B/question1.py) | Alpha-Beta Pruning with performance comparison | Alpha-Beta Pruning vs Minimax |
| **Set C - Q1** | [`Set C/question1.py`](Set%20C/question1.py) | Interactive Tic-Tac-Toe (Human vs AI) | Optimal Play using Minimax |

---

## Directory Structure

```text
Assignment-3/
├── README.md
├── Set A/
│   ├── question1.py
├── Set B/
│   ├── question1.py
└── Set C/
    └── question1.py
```

---

## Detailed Problem Explanations & Running Instructions

### Set A — Minimax Algorithm

#### Question 1: Minimax with Depth Limit
- **File:** `Set A/question1.py`
- **Objective:** Evaluate utility values on a game tree from the perspective of the MAX player. MIN alternates by minimizing the utility, and MAX selects the move leading to maximum payoff.
- **Run:**
  ```bash
  python "Assignment-3/Set A/question1.py"
  ```
- **Sample Output:**
  ```text
  Move to B gives utility: 3
  Move to C gives utility: 2

  Optimal move for MAX is to move to B
  Optimal utility value: 3
  ```

---

### Set B — Alpha-Beta Pruning

#### Question 1: Alpha-Beta Pruning with Performance Metrics
- **File:** `Set B/question1.py`
- **Objective:** Enhance Minimax with alpha ($\alpha$, best already explored option for MAX) and beta ($\beta$, best already explored option for MIN) cutoffs. Tracks pruned subtrees and compares the total number of node expansions between Minimax and Alpha-Beta.
- **Run:**
  ```bash
  python "Assignment-3/Set B/question1.py"
  ```
- **Sample Output:**
  ```text
  Minimax Results:
  Optimal Value: 3
  Total Nodes Visited (Minimax): 7

  Alpha-Beta Pruning Results:
  Optimal Value: 3
  Total Nodes Visited (Alpha-Beta): 5
  Pruned Nodes: ['G']

  Comparison:
  Minimax evaluated 7 nodes.
  Alpha-Beta evaluated 5 nodes.
  Alpha-Beta saved 2 node evaluations!
  ```

---

### Set C — Real-Time Game Application

#### Question 1: Tic-Tac-Toe Game (Human vs AI)
- **File:** `Set C/question1.py`
- **Objective:** Play an interactive console game of Tic-Tac-Toe against the computer. The computer evaluates all legal board configurations recursively via Minimax to guarantee that the AI never loses (either wins or draws).
- **Run:**
  ```bash
  python "Assignment-3/Set C/question1.py"
  ```
- **Sample Interaction:**
  ```text
   0 | 1 | 2
  ---+---+---
   3 | 4 | 5
  ---+---+---
   6 | 7 | 8

  Enter your move (0-8): 4
  Computer played at position 0
  ...
  Result: Draw / Computer Wins
  ```

---

## Viva Questions & Answers

1. **What is a zero-sum game?**
   - A zero-sum game is a mathematical representation where the total payoff is constant, meaning one player's gain is exactly equal to the other player's loss.
2. **What are $\alpha$ and $\beta$ in Alpha-Beta pruning?**
   - $\alpha$ is the minimum score that the maximizing player is assured of.
   - $\beta$ is the maximum score that the minimizing player is assured of.
   - Pruning occurs when $\alpha \ge \beta$.
3. **What is the time complexity improvement of Alpha-Beta over Minimax?**
   - Standard Minimax takes $O(b^m)$ time. With optimal move ordering, Alpha-Beta pruning reduces the search complexity to $O(b^{m/2})$, effectively doubling the searchable depth in the same amount of time.
4. **Why is Tic-Tac-Toe always a draw under optimal play?**
   - Under perfect play by both players (using Minimax), the game-theoretic value of Tic-Tac-Toe from the initial empty board is 0 (a draw).
