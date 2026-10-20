# Assignment 4: Neural Networks and Deep Learning

Based on Assignment 4 in the M.Sc. Computer Science AI practical lab book (Academic Year 2026–2027).

---

## Practicals Overview

| Set | File | Topic / Problem Statement | Architecture / Libraries |
|---|---|---|---|
| **Set A - Q1** | [`Set A/question1.py`](Set%20A/question1.py) | Perceptron learning for binary 2-input AND and OR gates | Single-Layer Perceptron (Binary) |
| **Set A - Q2** | [`Set A/question2.py`](Set%20A/question2.py) | Perceptron for bipolar 2-input AND gate ({-1, 1}) | Single-Layer Perceptron (Bipolar) |
| **Set B - Q1** | [`Set B/question1.py`](Set%20B/question1.py) | Multi-Layer Perceptron (MLP) for XOR with Backpropagation | MLP (2-4-1), Sigmoid, NumPy |
| **Set C - Q1** | [`Set C/question1.py`](Set%20C/question1.py) | 3-Layer Deep Neural Network on Iris dataset with 10, 100, 1000 epochs | Keras / TensorFlow, Scikit-Learn |

---

## Directory Structure

```text
Assignment-4/
├── README.md
├── Set A/
│   ├── question1.py
│   └── question2.py
├── Set B/
│   ├── question1.py
└── Set C/
    └── question1.py
```

---

## Detailed Problem Explanations & Running Instructions

### Set A — Single-Layer Perceptron

#### Question 1: Binary Perceptron for AND and OR Gates
- **File:** `Set A/question1.py`
- **Objective:** Train a single perceptron using the delta learning rule on binary inputs $(0, 1)$ to find the decision boundary for linearly separable functions: AND and OR.
- **Run:**
  ```bash
  python "Assignment-4/Set A/question1.py"
  ```
- **Sample Output:**
  ```text
  AND Gate
  Final weights: [0.2, 0.1]
  Final bias: -0.2
  Epochs required: 6

  OR Gate
  Final weights: [0.1, 0.1]
  Final bias: 0.0
  Epochs required: 4
  ```

#### Question 2: Bipolar Perceptron for AND Gate
- **File:** `Set A/question2.py`
- **Objective:** Train a perceptron using bipolar inputs and targets $x_i, y \in \{-1, +1\}$ with step activation $y = 1 \text{ if } net \ge 0 \text{ else } -1$, printing epoch-by-epoch convergence.
- **Run:**
  ```bash
  python "Assignment-4/Set A/question2.py"
  ```
- **Sample Output:**
  ```text
  Bipolar AND Gate Training
  Epoch: 1 | w1: 0.2 | w2: 0.2 | Bias: -0.2 | Errors: 2
  Epoch: 2 | w1: 0.2 | w2: 0.2 | Bias: -0.2 | Errors: 0

  Final Weights:
  w1 = 0.2
  w2 = 0.2
  Bias = -0.2
  ```

---

### Set B — Multi-Layer Perceptron (MLP) & Backpropagation

#### Question 1: XOR Classification using MLP
- **File:** `Set B/question1.py`
- **Objective:** Solve the classic non-linearly separable XOR problem using a 2-4-1 Multi-Layer Perceptron with Sigmoid activations and Gradient Descent Backpropagation in pure NumPy.
- **Run:**
  ```bash
  python "Assignment-4/Set B/question1.py"
  ```
- **Sample Output:**
  ```text
  XOR Inputs and Outputs:
  [0, 0] -> 0.04  (Expected: 0)
  [0, 1] -> 0.96  (Expected: 1)
  [1, 0] -> 0.95  (Expected: 1)
  [1, 1] -> 0.05  (Expected: 0)
  Final Loss: 0.003
  ```

---

### Set C — Deep Neural Networks with Keras

#### Question 1: 3-Layer Classifier on Iris Dataset across Epochs
- **File:** `Set C/question1.py`
- **Objective:** Construct a 3-layer neural network using Keras (Input 4 features $\to$ Dense 10 neurons with ReLU $\to$ Dense 3 neurons with Softmax) on the Iris dataset. Train separately for 10, 100, and 1000 epochs, evaluating accuracy and loss to measure the impact of training iterations.
- **Dependencies:**
  ```bash
  pip install tensorflow scikit-learn numpy
  ```
- **Run:**
  ```bash
  python "Assignment-4/Set C/question1.py"
  ```
- **Sample Output / Comparison Table:**
  ```text
  ==============================================================
  Epochs       Training Loss      Training Accuracy   Test Accuracy
  ==============================================================
  10           0.8712             72.50%              70.00%
  100          0.1248             96.67%              96.67%
  1000         0.0381             99.17%              96.67%
  ==============================================================
  ```

---

## Viva Questions & Answers

1. **Why can't a single-layer perceptron solve the XOR problem?**
   - A single-layer perceptron can only form a single linear hyperplane (linear decision boundary). XOR is non-linearly separable as no single straight line can separate $(0,1), (1,0)$ from $(0,0), (1,1)$.
2. **What is the purpose of activation functions?**
   - Activation functions introduce non-linearity into the network, enabling multi-layer networks to learn complex non-linear mappings. Without non-linear activation functions, stacked linear layers collapse into a single linear transformation.
3. **What is Backpropagation?**
   - Backpropagation is the algorithm that computes the gradient of the loss function with respect to each weight and bias using the calculus chain rule, propagating errors backwards from the output layer to input layers to update weights via gradient descent.
4. **How does epoch count affect underfitting and overfitting?**
   - Too few epochs (e.g. 10) causes underfitting because weights have not converged to minimal error.
   - An appropriate number of epochs (e.g. 100) balances high training and test accuracy.
   - Excessively large epoch counts (e.g. 1000+) can lead to overfitting, where the model memorizes training noise and generalizes less effectively.
