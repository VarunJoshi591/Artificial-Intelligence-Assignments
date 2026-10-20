#Write a program to implement a Multi-Layer Perceptron (MLP) with a single hidden layer to 
#solve the XOR problem (which is not linearly separable). Use the Backpropagation algorithm 
#for training.


# Assignment 4 - Set B - Question 1

import numpy as np

# XOR input and target data
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
], dtype=float)

Y = np.array([
    [0],
    [1],
    [1],
    [0]
], dtype=float)

# Network architecture: 2 inputs, 4 hidden neurons, 1 output
np.random.seed(42)

W1 = np.random.randn(2, 4)
b1 = np.zeros((1, 4))

W2 = np.random.randn(4, 1)
b2 = np.zeros((1, 1))

learning_rate = 0.5
epochs = 10000


# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Training using backpropagation
for epoch in range(epochs):

    # Forward propagation
    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    predicted_output = sigmoid(final_input)

    # Calculate output error
    output_error = predicted_output - Y

    # Backpropagation
    d_output = output_error * predicted_output * (1 - predicted_output)

    hidden_error = np.dot(d_output, W2.T)
    d_hidden = hidden_error * hidden_output * (1 - hidden_output)

    # Update weights and biases
    W2 -= learning_rate * np.dot(hidden_output.T, d_output) / len(X)
    b2 -= learning_rate * np.mean(d_output, axis=0, keepdims=True)

    W1 -= learning_rate * np.dot(X.T, d_hidden) / len(X)
    b1 -= learning_rate * np.mean(d_hidden, axis=0, keepdims=True)


# Test the trained network
hidden_output = sigmoid(np.dot(X, W1) + b1)
predicted_output = sigmoid(np.dot(hidden_output, W2) + b2)

print("XOR using Multi-Layer Perceptron")
print("\nInput\t\tTarget\tPredicted")

for i in range(len(X)):
    prediction = 1 if predicted_output[i, 0] >= 0.5 else 0

    print(
        X[i].astype(int),
        "\t", int(Y[i, 0]),
        "\t", prediction
    )

print("\nTraining completed for", epochs, "epochs.")
