
import numpy as np
from sklearn.metrics import log_loss

def sigmoid(z):
    """
    Sigmoid activation function.
    z: Input value or array
    Returns: Probability between 0 and 1
    """
    return 1 / (1 + np.exp(-z))

def manual_log_loss(y_true, y_pred_prob):
    """
    Manual implementation of Log-Loss (Binary Cross-Entropy).
    J(theta) = -1/m * sum(y*log(h(x)) + (1-y)*log(1-h(x)))
    
    y_true: Actual labels (0 or 1)
    y_pred_prob: Predicted probabilities
    
    Returns: Cost value
    """
    m = len(y_true)
    # Add a small epsilon to avoid log(0) errors
    epsilon = 1e-15
    y_pred_prob = np.clip(y_pred_prob, epsilon, 1 - epsilon)
    
    cost = -1/m * np.sum(y_true * np.log(y_pred_prob) + (1 - y_true) * np.log(1 - y_pred_prob))
    return cost

def run_verification():
    # 1. Synthetic Data Generation
    print("Generating Synthetic Data...")
    hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # Let's assume a simple threshold around 5 hours for pass/fail
    # Fail (0) for < 5, Pass (1) for >= 5
    y_true = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    
    print(f"Hours: {hours_studied}")
    print(f"Labels: {y_true}")

    # 2. Simulate Predictions (using a linear function converted to probability via sigmoid)
    # z = mx + b (Let's say m=1, b=-5.5 to shift transition to around 5.5)
    z = 1.0 * hours_studied - 5.5
    y_pred_prob = sigmoid(z)
    
    print(f"\nPredicted Probabilities:\n{y_pred_prob}")
    
    # 3. Calculate Manual Log-Loss
    manual_loss = manual_log_loss(y_true, y_pred_prob)
    print(f"\nManual Log-Loss: {manual_loss}")
    
    # 4. Calculate Sklearn Log-Loss
    sklearn_loss = log_loss(y_true, y_pred_prob)
    print(f"Sklearn Log-Loss: {sklearn_loss}")
    
    # 5. Verification
    difference = abs(manual_loss - sklearn_loss)
    print(f"\nDifference: {difference}")
    
    assert difference < 1e-10, "Discrepancy too large between manual and sklearn log-loss!"
    print("\n✅ Verification Successful: Manual implementation matches Sklearn.")

if __name__ == "__main__":
    run_verification()
