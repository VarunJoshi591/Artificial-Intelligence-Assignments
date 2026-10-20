#Implement a Perceptron for a 2-input AND gate using bipolar inputs (-1 and 1) and bipolar 
#targets
#(-1 and 1). Show the training process and the final weights


# Bipolar AND Gate using Perceptron

def train_bipolar_and():
    # Bipolar input combinations
    X = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Bipolar target outputs
    targets = [-1, -1, -1, 1]

    # Initialize weights and bias
    w1 = 0.0
    w2 = 0.0
    bias = 0.0

    learning_rate = 0.1
    max_epochs = 100

    print("Bipolar AND Gate Training")

    for epoch in range(1, max_epochs + 1):
        errors = 0

        for inputs, target in zip(X, targets):
            x1, x2 = inputs

            # Calculate weighted sum
            net = x1 * w1 + x2 * w2 + bias

            # Bipolar step activation function
            output = 1 if net >= 0 else -1

            # Calculate error
            error = target - output

            # Update weights and bias
            if error != 0:
                w1 += learning_rate * error * x1
                w2 += learning_rate * error * x2
                bias += learning_rate * error
                errors += 1

        print(
            "Epoch:", epoch,
            "| w1:", round(w1, 2),
            "| w2:", round(w2, 2),
            "| Bias:", round(bias, 2),
            "| Errors:", errors
        )

        # Stop when all patterns are classified correctly
        if errors == 0:
            break

    print("\nFinal Weights:")
    print("w1 =", round(w1, 2))
    print("w2 =", round(w2, 2))
    print("Bias =", round(bias, 2))
    print("Epochs required:", epoch)

    print("\nFinal Output:")
    for inputs in X:
        x1, x2 = inputs
        net = x1 * w1 + x2 * w2 + bias
        output = 1 if net >= 0 else -1
        print(inputs, "->", output)


train_bipolar_and()
