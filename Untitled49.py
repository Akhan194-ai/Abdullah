#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset from the Excel file
file_path = 'AITASK1.xlsx'  # Replace with your file path if needed
df = pd.read_excel(file_path)

# Encode the 'Gender' column as 0 (female) and 1 (male)
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

# Prepare features (X) and target (y)
X = df[['Height', 'Weight', 'Foot_Size']].values
y = df['Gender'].values

# Train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Function to predict gender based on new entry
def predict_gender(height, weight, foot_size):
    prediction = clf.predict([[height, weight, foot_size]])
    return le.inverse_transform(prediction)[0]

# Example of predicting gender for a new entry
new_height = 5.5    # Example input
new_weight = 130    # Example input
new_foot_size = 8   # Example input

predicted_gender = predict_gender(new_height, new_weight, new_foot_size)
print("Predicted Gender for the new entry:", predicted_gender)


# In[ ]:




