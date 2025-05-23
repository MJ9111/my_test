import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("Script started")

# Load the data from CSV
data = pd.read_csv('spam_predictions.csv', sep=';')

print("Data loaded:")
print(data.head())  # show first 5 rows to check

# Extract true and predicted labels
y_true = data['text_label']
y_pred = data['pred_label']

# Calculate metrics for the 'spam' class
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, pos_label='spam')
recall = recall_score(y_true, y_pred, pos_label='spam')
f1 = f1_score(y_true, y_pred, pos_label='spam')

# Print results
print(f"\nAccuracy: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-score: {f1:.3f}")
