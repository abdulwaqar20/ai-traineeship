"""
Task 3.1 - Neural Network from Scratch (XOR Problem)

Backpropagation
---------------------------------
Backpropagation is the process that allows a neural network to learn from its
mistakes. After making predictions, the network calculates how far those
predictions are from the correct answers using a loss function. It then works
backwards through the network to determine how much each weight contributed to
the error. Using these gradients, every weight and bias is updated in the
direction that reduces the loss. Repeating this process over many epochs allows
the network to gradually improve its predictions and learn the XOR function.
"""

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# XOR Dataset
# ----------------------------
X = np.array([[0, 0],[0, 1],[1, 0],[1, 1]], dtype=float)
y = np.array([[0],[1],[1],[0]], dtype=float)

# Hyperparameters
np.random.seed(42)

input_size = 2
hidden_size = 4
output_size = 1

learning_rate = 0.2
epochs = 10000

# Weight Initialization
W1 = np.random.randn(input_size, hidden_size) * np.sqrt(1 / input_size)
b1 = np.zeros((1, hidden_size))

W2 = np.random.randn(hidden_size, output_size) * np.sqrt(1 / hidden_size)
b2 = np.zeros((1, output_size))

# Activation Function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(output):
    return output * (1 - output)

loss_history = []

# Training Loop
for epoch in range(epochs):

    # Forward Pass
    z1 = np.dot(X, W1) + b1
    a1 = sigmoid(z1)

    z2 = np.dot(a1, W2) + b2
    predictions = sigmoid(z2)

    # Loss (MSE)
    loss = np.mean((predictions - y) ** 2)
    loss_history.append(loss)

    # Backpropagation

    # Output layer
    d_output = (predictions - y) * sigmoid_derivative(predictions)

    m = X.shape[0]

    dW2 = np.dot(a1.T, d_output) / m
    db2 = np.sum(d_output, axis=0, keepdims=True) / m

    # Hidden layer
    d_hidden = np.dot(d_output, W2.T) * sigmoid_derivative(a1)

    dW1 = np.dot(X.T, d_hidden) / m
    db1 = np.sum(d_hidden, axis=0, keepdims=True) / m

    # Gradient Descent
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if epoch % 500 == 0:
        print(f"Epoch {epoch:4d} | Loss = {loss:.6f}")

# Final Predictions

print("\nFinal Predictions\n")

z1 = np.dot(X, W1) + b1
a1 = sigmoid(z1)

z2 = np.dot(a1, W2) + b2
predictions = sigmoid(z2)

for inp, pred in zip(X, predictions):
    print(f"{inp} -> {pred[0]:.4f}")

# Accuracy
binary_predictions = (predictions >= 0.5).astype(int)
accuracy = np.mean(binary_predictions == y) * 100

print(f"\nAccuracy: {accuracy:.2f}%")

# Plot Loss Curve
plt.figure(figsize=(8,5))
plt.plot(loss_history)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.grid(True)
plt.tight_layout()

plt.savefig("loss_curve.png")
plt.show()