#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Dataset provided
data = {
    'Product Name': [
        'Electric Kettle', 'Air Fryer', 'Vacuum Cleaner', 'Coffee Maker', 
        'Blender', 'Toaster', 'Rice Cooker', 'Iron', 'Microwave Oven', 'Dish Washer'
    ],
    'Price': [
        'Affordable', 'Expensive', 'Premium', 'Affordable', 
        'Affordable', 'Low-cost', 'Mid-range', 'Affordable', 'Expensive', 'Premium'
    ],
    'Rating': [
        'High', 'Very High', 'Moderate', 'High', 
        'Moderate', 'Low', 'Moderate', 'High', 'High', 'Very High'
    ],
    'Reviews': [
        'Many', 'Numerous', 'Few', 'Many', 
        'Several', 'Some', 'Many', 'Some', 'Many', 'Numerous'
    ],
    'Purchased': [
        'Yes', 'Yes', 'No', 'Yes', 
        'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes'
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Define the features and target
features = ['Price', 'Rating', 'Reviews']
target = 'Purchased'

# Function to calculate the probability
def calculate_probability(df, feature, value, target, target_value):
    feature_df = df[df[target] == target_value]
    probability = len(feature_df[feature_df[feature] == value]) / len(feature_df)
    return probability

# Calculate prior probabilities
p_yes = len(df[df[target] == 'Yes']) / len(df)
p_no = len(df[df[target] == 'No']) / len(df)

# Define the new product attributes for prediction
new_product = {'Price': 'Expensive', 'Rating': 'Very High', 'Reviews': 'Many'}

# Calculate conditional probabilities for "Yes"
p_price_yes = calculate_probability(df, 'Price', new_product['Price'], target, 'Yes')
p_rating_yes = calculate_probability(df, 'Rating', new_product['Rating'], target, 'Yes')
p_reviews_yes = calculate_probability(df, 'Reviews', new_product['Reviews'], target, 'Yes')

# Calculate conditional probabilities for "No"
p_price_no = calculate_probability(df, 'Price', new_product['Price'], target, 'No')
p_rating_no = calculate_probability(df, 'Rating', new_product['Rating'], target, 'No')
p_reviews_no = calculate_probability(df, 'Reviews', new_product['Reviews'], target, 'No')

# Calculate the total probability for "Yes" and "No"
p_yes_given_product = p_yes * p_price_yes * p_rating_yes * p_reviews_yes
p_no_given_product = p_no * p_price_no * p_rating_no * p_reviews_no

# Determine the prediction
if p_yes_given_product > p_no_given_product:
    prediction = 'Yes'
else:
    prediction = 'No'

# Output the prediction
print(f"Prediction for purchasing the product with attributes {new_product}: {prediction}")


# In[ ]:




