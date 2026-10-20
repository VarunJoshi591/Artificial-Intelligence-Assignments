# Assignment 2: Knowledge Representation and Reasoning

Based on Assignment 2 in the M.Sc. Computer Science AI practical lab book (Academic Year 2026–2027).

---

## Practicals Overview

| Set | File | Topic / Problem Statement | Technique / Logic Form |
|---|---|---|---|
| **Set A - Q1** | [`Set A/question1.py`](Set%20A/question1.py) | Family Tree Knowledge Base & Relationship Rules | First-Order Relations (Prolog style in Python) |
| **Set A - Q2** | [`Set A/question2.py`](Set%20A/question2.py) | Resolution Refutation (Socrates is mortal) | Propositional / Predicate Resolution |
| **Set B - Q1** | [`Set B/question1.py`](Set%20B/question1.py) | Resolution Refutation in First-Order Logic with CNF | Automated CNF Resolution & Contradiction Detection |
| **Set C - Q1** | [`Set C/question1.py`](Set%20C/question1.py) | Knowledge Representation using Semantic Networks | Directed Graph with `is-a` & `has-a` Inheritance Queries |

---

## Directory Structure

```text
Assignment-2/
├── README.md
├── Set A/
│   ├── question1.py
│   └── question2.py
├── Set B/
│   └── question1.py
└── Set C/
    └── question1.py
```

---

## Detailed Problem Explanations & Running Instructions

### Set A — Basic Knowledge Representation & Resolution

#### Question 1: Family Tree Knowledge Base
- **File:** `Set A/question1.py`
- **Objective:** Model a family hierarchy with base facts (`parents`, `males`, `females`) and relational deduction rules (`mother`, `father`, `sibling`, `grandparent`).
- **Run:**
  ```bash
  python "Assignment-2/Set A/question1.py"
  ```
- **Sample Output:**
  ```text
  Is Mary mother of Alice? True
  Is John father of Bob? True
  Are Alice and Bob siblings? True
  Is John grandparent of David? True
  ```

#### Question 2: Resolution Refutation Example
- **File:** `Set A/question2.py`
- **Objective:** Prove the classic deductive syllogism:
  1. All humans are mortal: $\neg Human(x) \lor Mortal(x)$
  2. Socrates is human: $Human(Socrates)$
  3. Prove: $Mortal(Socrates)$ by adding negation $\neg Mortal(Socrates)$ and reaching the empty clause ($\square$).
- **Run:**
  ```bash
  python "Assignment-2/Set A/question2.py"
  ```
- **Sample Output:**
  ```text
  Initial Clauses:
  {'Mortal(x)', 'NOT Human(x)'}
  {'Human(Socrates)'}
  {'NOT Mortal(Socrates)'}

  Resolution Steps:
  1. Human(Socrates)
  2. NOT Human(x) OR Mortal(x)
  --------------------------------
  3. Mortal(Socrates)

  Now:
  Mortal(Socrates)
  NOT Mortal(Socrates)
  --------------------------------
  Empty Clause: {}

  Conclusion:
  The statement 'Socrates is mortal' is TRUE.
  ```

---

### Set B — Automated First-Order Resolution Refutation

#### Question 1: Resolution Refutation in First-Order Logic
- **File:** `Set B/question1.py`
- **Objective:** Convert sentences into Conjunctive Normal Form (CNF) clauses and apply resolution iteratively between complementary literals until an empty clause is found (proving contradiction).
- **Run:**
  ```bash
  python "Assignment-2/Set B/question1.py"
  ```
- **Sample Output:**
  ```text
  Initial CNF Clauses:
  ['~P', 'Q']
  ['P']
  ['~Q']

  Resolution Steps:
  ['~P', 'Q'] + ['P'] => ['Q']
  ['Q'] + ['~Q'] => []

  Contradiction found!
  Statement is PROVED.
  ```

---

### Set C — Semantic Networks & Property Inheritance

#### Question 1: Semantic Network with Inheritance
- **File:** `Set C/question1.py`
- **Objective:** Represent hierarchical knowledge using a graph with entities (`Animal`, `Dog`, `Cat`, `Bird`) linked by `is-a` relationships and annotated with `has-a` attributes, resolving inheritance queries recursively.
- **Run:**
  ```bash
  python "Assignment-2/Set C/question1.py"
  ```
- **Sample Output:**
  ```text
  Semantic Network:
  Animal : {'is-a': [], 'has-a': ['four legs']}
  Dog : {'is-a': ['Animal'], 'has-a': []}
  Cat : {'is-a': ['Animal'], 'has-a': []}
  Bird : {'is-a': ['Animal'], 'has-a': ['two wings']}

  Inheritance Queries:
  Does a dog have four legs? Yes
  Does a cat have four legs? Yes
  Does a bird have two wings? Yes
  Does a dog have two wings? No
  ```

---

## Viva Questions & Answers

1. **What is the Resolution Principle in First-Order Logic?**
   - Resolution is an inference rule that derives a new clause from two clauses containing complementary literals: $(A \lor B) \land (\neg B \lor C) \models (A \lor C)$.
2. **Why do we negate the goal in Resolution Refutation?**
   - By assuming the negation of the theorem and combining it with the knowledge base, deriving an empty clause (contradiction) mathematically proves that the original theorem must be true (proof by contradiction / reductio ad absurdum).
3. **What is Conjunctive Normal Form (CNF)?**
   - CNF is a conjunction of one or more clauses, where each clause is a disjunction of literals (e.g., $(A \lor B) \land (\neg C \lor D)$).
4. **How does property inheritance work in Semantic Networks?**
   - Subordinate nodes inherit properties from superordinate nodes along taxonomic links (like `is-a`), allowing efficient representation without repeating common attributes.
