#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Data (Gender, Height, Weight, Foot_Size)
data = [
    ['male', 6.00, 180, 12],
    ['male', 5.92, 190, 11],
    ['male', 5.58, 170, 12],
    ['male', 5.92, 165, 10],
    ['female', 5.00, 100, 6],
    ['female', 5.50, 150, 8],
    ['female', 5.42, 130, 7],
    ['female', 5.75, 150, 9]
]

# Convert data into numpy array and encode 'Gender'
data = np.array(data)
X = data[:, 1:].astype(float)  # Features: Height, Weight, Foot_Size
y = np.array([0 if gender == 'female' else 1 for gender in data[:, 0]])  # Target: 0 (female), 1 (male)

# Function to calculate entropy
def entropy(y):
    class_labels = np.unique(y)
    entropy_val = 0
    for label in class_labels:
        prob = np.sum(y == label) / len(y)
        entropy_val -= prob * np.log2(prob)
    return entropy_val

# Function to split dataset based on a feature and threshold
def split_data(X, y, feature_index, threshold):
    left_mask = X[:, feature_index] <= threshold
    right_mask = ~left_mask
    X_left, X_right = X[left_mask], X[right_mask]
    y_left, y_right = y[left_mask], y[right_mask]
    return X_left, X_right, y_left, y_right

# Function to find the best split
def best_split(X, y):
    best_feature = None
    best_threshold = None
    best_info_gain = -1
    best_left_y = None
    best_right_y = None

    base_entropy = entropy(y)
    for feature_index in range(X.shape[1]):
        thresholds = np.unique(X[:, feature_index])
        for threshold in thresholds:
            X_left, X_right, y_left, y_right = split_data(X, y, feature_index, threshold)
            if len(y_left) == 0 or len(y_right) == 0:
                continue  # Skip if any split is empty
            
            # Calculate information gain
            left_entropy = entropy(y_left)
            right_entropy = entropy(y_right)
            weighted_entropy = (len(y_left) / len(y)) * left_entropy + (len(y_right) / len(y)) * right_entropy
            info_gain = base_entropy - weighted_entropy

            if info_gain > best_info_gain:
                best_info_gain = info_gain
                best_feature = feature_index
                best_threshold = threshold
                best_left_y = y_left
                best_right_y = y_right

    return best_feature, best_threshold, best_left_y, best_right_y

# Function to build the decision tree recursively
def build_tree(X, y, depth=0, max_depth=3):
    if len(np.unique(y)) == 1:  # All samples belong to the same class
        return {'label': y[0]}
    
    if depth >= max_depth:  # Stop if max depth is reached
        return {'label': np.bincount(y).argmax()}

    feature, threshold, left_y, right_y = best_split(X, y)
    if feature is None:
        return {'label': np.bincount(y).argmax()}  # Return most common label if no split found
    
    left_tree = build_tree(X[left_y == y], left_y, depth + 1, max_depth)
    right_tree = build_tree(X[right_y == y], right_y, depth + 1, max_depth)

    return {
        'feature': feature,
        'threshold': threshold,
        'left': left_tree,
        'right': right_tree
    }

# Function to predict using the decision tree
def predict(tree, sample):
    if 'label' in tree:
        return tree['label']
    
    feature_value = sample[tree['feature']]
    if feature_value <= tree['threshold']:
        return predict(tree['left'], sample)
    else:
        return predict(tree['right'], sample)

# Train the decision tree
tree = build_tree(X, y)

# Test the decision tree with a new sample
new_sample = np.array([5.5, 150, 8])  # Example: Height=5.5, Weight=150, Foot_Size=8
prediction = predict(tree, new_sample)
predicted_gender = 'female' if prediction == 0 else 'male'

print("Predicted Gender:", predicted_gender)


# In[ ]:




