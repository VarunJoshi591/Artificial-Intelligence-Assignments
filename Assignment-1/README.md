# Assignment 1: Problem Space, Search and Control Strategies

Based on Assignment 1 in the M.Sc. Computer Science AI practical lab book (Academic Year 2026–2027).

---

## Practicals Overview

| Set | File | Topic / Problem Statement | Algorithm / Technique |
|---|---|---|---|
| **Set A - Q1** | [`Set A/question1.py`](Set%20A/question1.py) | Tower of Hanoi for N disks | Recursive Depth-First Search (DFS) |
| **Set A - Q2** | [`Set A/question2.py`](Set%20A/question2.py) | Graph traversal & shortest path | Breadth-First Search (BFS) |
| **Set B - Q1** | [`Set B/question1.py`](Set%20B/question1.py) | Shortest path on Romania map with straight-line heuristic | A* Search Algorithm |
| **Set B - Q2** | [`Set B/question2.py`](Set%20B/question2.py) | Comparison of A* vs Greedy Best-First Search | Greedy Best-First vs A* ($f(n) = h(n)$) |
| **Set C - Q1** | [`Set C/question1.py`](Set%20C/question1.py) | 4-gallon & 3-gallon Water Jug Problem to reach 2 gallons | State Space Search (BFS) |

---

## Directory Structure

```text
Assignment-1/
├── README.md
├── Q01_AI_Problem_Characteristics.py
├── Set A/
│   ├── question1.py
│   └── question2.py
├── Set B/
│   ├── question1.py
│   └── question2.py
└── Set C/
    └── question1.py
```

---

## Detailed Problem Explanations & Running Instructions

### Set A — Uninformed Search

#### Question 1: Tower of Hanoi using DFS
- **File:** `Set A/question1.py`
- **Objective:** Solve the classic Tower of Hanoi problem for $N$ disks with 3 pegs (Source A, Auxiliary B, Destination C) using Depth-First Search (recursion).
- **Complexity:** $2^N - 1$ moves.
- **Run:**
  ```bash
  python "Assignment-1/Set A/question1.py"
  ```
- **Sample Run:**
  ```text
  Enter the number of disks: 3
  Move disk 1 from A to C
  Move disk 2 from A to B
  Move disk 1 from C to B
  Move disk 3 from A to C
  Move disk 1 from B to A
  Move disk 2 from B to C
  Move disk 1 from A to C
  Total number of moves: 7
  ```

#### Question 2: Breadth-First Search (BFS) on Graph
- **File:** `Set A/question2.py`
- **Objective:** Traverse an unweighted graph using an adjacency list and find the shortest path from start node to destination node.
- **Run:**
  ```bash
  python "Assignment-1/Set A/question2.py"
  ```
- **Sample Output:**
  ```text
  Traversal Order: ['A', 'B', 'C', 'D', 'E', 'F']
  Shortest Path: ['A', 'C', 'F']
  ```

---

### Set B — Informed (Heuristic) Search

#### Question 1: A* Search Algorithm
- **File:** `Set B/question1.py`
- **Objective:** Find the optimal shortest path between Arad and Bucharest on the simplified Romania map using evaluation function $f(n) = g(n) + h(n)$, where $g(n)$ is path cost and $h(n)$ is straight-line distance.
- **Run:**
  ```bash
  python "Assignment-1/Set B/question1.py"
  ```
- **Sample Output:**
  ```text
  A* Path: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
  Total Cost: 418
  ```

#### Question 2: Greedy Best-First Search vs A*
- **File:** `Set B/question2.py`
- **Objective:** Implement Greedy Best-First Search ($f(n) = h(n)$) and compare the total path cost and number of expanded nodes against A* search.
- **Run:**
  ```bash
  python "Assignment-1/Set B/question2.py"
  ```
- **Sample Output:**
  ```text
  A* Search:
  Path: ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
  Cost: 418
  Nodes Expanded: 5

  Greedy Best-First Search:
  Path: ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
  Cost: 450
  Nodes Expanded: 3
  ```

---

### Set C — State Space Search

#### Question 1: Water Jug Problem
- **File:** `Set C/question1.py`
- **Objective:** Measure exactly 2 gallons in the 4-gallon jug given a 4-gallon jug and a 3-gallon jug with unlimited water source, displaying the complete sequence of state transitions.
- **Run:**
  ```bash
  python "Assignment-1/Set C/question1.py"
  ```
- **Sample Output:**
  ```text
  Steps to reach the goal:
  (0, 0) -> (0, 3) -> (3, 0) -> (3, 3) -> (4, 2) -> (0, 2) -> (2, 0)
  ```

---

## Viva Questions & Answers

1. **What is an admissible heuristic in A* search?**
   - An admissible heuristic never overestimates the actual cost to reach the goal, guaranteeing that A* finds an optimal path.
2. **How does BFS differ from DFS in terms of optimality and space complexity?**
   - BFS is complete and finds the shallowest/shortest path in unweighted graphs, but requires $O(b^d)$ memory. DFS uses $O(bm)$ memory but is not guaranteed to find the shortest path.
3. **Why does Greedy Best-First Search expand fewer nodes but produce a sub-optimal path compared to A*?**
   - Greedy Best-First only considers $h(n)$ (estimated distance to goal) and ignores $g(n)$ (cost accrued so far), causing it to take short-sighted decisions.
