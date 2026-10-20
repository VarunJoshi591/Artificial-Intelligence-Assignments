#Implement a 3-layer Neural Network using the Keras library on a suitable classification 
#dataset from an online repository (e.g., Iris, or a small dataset from Kaggle). Train the model 
#separately for 10, 100, and 1000 epochs, and submit the code and a comparison table of the 
#training accuracy and loss at the end of each run to evaluate the impact of epochs.


# Assignment 4 - Set C - Question 1
# Three-Layer Neural Network using Keras
# Dataset: Iris

import numpy as np
from tensorflow.keras.utils import set_random_seed

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Input, Dense

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

epoch_values = [10, 100, 1000]
results = []

for epochs in epoch_values:

    # Reset the seed for a reproducible initialization
    set_random_seed(42)

    # Build a three-layer neural network
    model = Sequential([
        Input(shape=(4,)),
        Dense(10, activation="relu"),
        Dense(3, activation="softmax")
    ])

    # Compile the model
    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Train the model
    model.fit(
        X_train,
        y_train,
        epochs=epochs,
        batch_size=8,
        verbose=0
    )

    # Evaluate training accuracy and loss
    loss, accuracy = model.evaluate(
        X_train, y_train, verbose=0
    )

    # Evaluate test accuracy as an additional measure
    test_loss, test_accuracy = model.evaluate(
        X_test, y_test, verbose=0
    )

    results.append(
        (epochs, accuracy, loss, test_accuracy, test_loss)
    )

# Display the comparison table
print("\nComparison of Neural Network Training")
print("-" * 76)
print(
    f"{'Epochs':<10}"
    f"{'Train Accuracy':<18}"
    f"{'Train Loss':<15}"
    f"{'Test Accuracy':<18}"
    f"{'Test Loss':<12}"
)
print("-" * 76)

for epochs, acc, loss, test_acc, test_loss in results:
    print(
        f"{epochs:<10}"
        f"{acc:<18.4f}"
        f"{loss:<15.4f}"
        f"{test_acc:<18.4f}"
        f"{test_loss:<12.4f}"
    )

print("\nTraining and comparison completed.")
