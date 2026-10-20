# Artificial Intelligence Assignments

Practical programs, algorithms, and study notes for **M.Sc. Computer Science Part-I, Semester I** — *Practical Based on Artificial Intelligence* (Academic Year 2026–2027).

---

## Assignments Index

| No. | Assignment Title | Topics & Practicals Covered | Link |
|:---:|---|---|:---:|
| **1** | **Problem Space, Search and Control Strategies** | Tower of Hanoi (DFS), BFS on Graph, A* Search on Romania Map, Greedy Best-First Search, Water Jug Problem | [📁 Assignment-1](./Assignment-1/) |
| **2** | **Knowledge Representation & Reasoning** | Family Tree Knowledge Base, Resolution Refutation (Socrates Syllogism), First-Order CNF Resolution, Semantic Networks with Inheritance | [📁 Assignment-2](./Assignment-2/) |
| **3** | **Adversarial Search & Game Playing** | Minimax Algorithm with Depth Limit, Alpha-Beta Pruning with Performance Metrics, Interactive Tic-Tac-Toe Game (Human vs AI) | [📁 Assignment-3](./Assignment-3/) |
| **4** | **Neural Networks & Deep Learning** | Binary Single-Layer Perceptron (AND/OR), Bipolar Perceptron (AND), Multi-Layer Perceptron (MLP) for XOR with Backpropagation, 3-Layer Keras Deep Neural Network on Iris Dataset | [📁 Assignment-4](./Assignment-4/) |

---

## Repository Structure

```text
Artificial-Intelligence-Assignments/
├── README.md
├── .gitignore
├── Assignment-1/
│   ├── README.md
│   ├── Q01_AI_Problem_Characteristics.py
│   ├── Set A/
│   │   ├── question1.py        # Tower of Hanoi (DFS)
│   │   └── question2.py        # Breadth-First Search (BFS)
│   ├── Set B/
│   │   ├── question1.py        # A* Search Algorithm
│   │   └── question2.py        # Greedy Best-First Search vs A*
│   └── Set C/
│       └── question1.py        # Water Jug Problem (BFS)
│
├── Assignment-2/
│   ├── README.md
│   ├── Set A/
│   │   ├── question1.py        # Family Tree Relations (Prolog style)
│   │   └── question2.py        # Resolution Refutation (Socrates Syllogism)
│   ├── Set B/
│   │   └── question1.py        # First-Order Logic Resolution in CNF
│   └── Set C/
│       └── question1.py        # Semantic Network with Property Inheritance
│
├── Assignment-3/
│   ├── README.md
│   ├── Set A/
│   │   └── question1.py        # Minimax with Fixed Depth Limit
│   ├── Set B/
│   │   └── question1.py        # Alpha-Beta Pruning with Performance Metrics
│   └── Set C/
│       └── question1.py        # Interactive Tic-Tac-Toe Game (Minimax)
│
└── Assignment-4/
    ├── README.md
    ├── Set A/
    │   ├── question1.py        # Binary Perceptron (AND & OR Gates)
    │   └── question2.py        # Bipolar Perceptron (AND Gate)
    ├── Set B/
    │   └── question1.py        # Multi-Layer Perceptron (MLP) for XOR
    └── Set C/
        └── question1.py        # 3-Layer Keras Neural Network (Iris Dataset)
```

---

## Getting Started

### 1. Prerequisites
- Python 3.9+ installed.

### 2. Virtual Environment Setup
```bash
# Clone the repository
git clone https://github.com/VarunJoshi591/Artificial-Intelligence-Assignments.git
cd Artificial-Intelligence-Assignments

# Create and activate a virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies
Assignments 1 to 3 use standard Python library modules (`heapq`, `collections`, `random`).  
Assignment 4 requires numeric computing and machine learning packages:
```bash
pip install numpy scikit-learn tensorflow
```

---

## Running the Practicals

You can execute any practical by navigating to the repository root and running the script:

```bash
# Assignment 1 - Breadth-First Search
python "Assignment-1/Set A/question2.py"

# Assignment 2 - Semantic Network
python "Assignment-2/Set C/question1.py"

# Assignment 3 - Interactive Tic-Tac-Toe
python "Assignment-3/Set C/question1.py"

# Assignment 4 - XOR Multi-Layer Perceptron
python "Assignment-4/Set B/question1.py"
```

Each assignment folder contains a dedicated `README.md` with:
- Formal question & objective
- Algorithm explanations & complexity
- Sample console outputs
- Viva preparation questions & answers
