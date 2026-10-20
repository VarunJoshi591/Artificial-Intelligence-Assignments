#Write a Python program to implement a Perceptron that can learn the weights and bias for a 2-
#input AND gate and a 2-input OR gate with binary inputs (0 and 1). Show the final weights 
#and the number of epochs required for convergence.


# Perceptron for AND and OR Gates

def train_perceptron(X, targets, learning_rate=0.1):
    weights = [0.0, 0.0]
    bias = 0.0
    max_epochs = 100

    for epoch in range(1, max_epochs + 1):
        errors = 0

        for inputs, target in zip(X, targets):
            x1, x2 = inputs

            # Calculate weighted sum
            net = (x1 * weights[0] +
                   x2 * weights[1] + bias)

            # Step activation function
            output = 1 if net > 0 else 0

            # Calculate error
            error = target - output

            # Update weights and bias
            if error != 0:
                weights[0] += learning_rate * error * x1
                weights[1] += learning_rate * error * x2
                bias += learning_rate * error
                errors += 1

        # Stop when all training examples are correct
        if errors == 0:
            return weights, bias, epoch

    return weights, bias, max_epochs


# Binary input combinations
X = [(0, 0), (0, 1), (1, 0), (1, 1)]

and_targets = [0, 0, 0, 1]
or_targets = [0, 1, 1, 1]

# Train AND gate
and_weights, and_bias, and_epochs = train_perceptron(
    X, and_targets
)

# Train OR gate
or_weights, or_bias, or_epochs = train_perceptron(
    X, or_targets
)

print("AND Gate")
print("Final weights:", and_weights)
print("Final bias:", round(and_bias, 2))
print("Epochs required:", and_epochs)

print("\nOR Gate")
print("Final weights:", or_weights)
print("Final bias:", round(or_bias, 2))
print("Epochs required:", or_epochs)
