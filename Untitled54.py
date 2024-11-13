#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Dataset in numpy format, without Pandas
data = {
    'Product Name': ['Electric Kettle', 'Air Fryer', 'Vacuum Cleaner', 'Coffee Maker', 
                     'Blender', 'Toaster', 'Rice Cooker', 'Iron', 'Microwave Oven', 'Dish Washer'],
    'Price': ['Affordable', 'Expensive', 'Premium', 'Affordable', 
              'Affordable', 'Low-cost', 'Mid-range', 'Affordable', 'Expensive', 'Premium'],
    'Rating': ['High', 'Very High', 'Moderate', 'High', 
               'Moderate', 'Low', 'Moderate', 'High', 'High', 'Very High'],
    'Reviews': ['Many', 'Numerous', 'Few', 'Many', 
                'Several', 'Some', 'Many', 'Some', 'Many', 'Numerous'],
    'Purchased': ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

# Encode categorical features and target variable
le_price = LabelEncoder()
le_rating = LabelEncoder()
le_reviews = LabelEncoder()
le_purchased = LabelEncoder()

# Transform categorical features into numerical values
price_encoded = le_price.fit_transform(data['Price'])
rating_encoded = le_rating.fit_transform(data['Rating'])
reviews_encoded = le_reviews.fit_transform(data['Reviews'])
purchased_encoded = le_purchased.fit_transform(data['Purchased'])

# Stack features into a single numpy array
X = np.column_stack((price_encoded, rating_encoded, reviews_encoded))
y = purchased_encoded

# Initialize and train the Decision Tree Classifier
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Function to predict if a product will be purchased based on new feature data
def predict_purchase(price, rating, reviews):
    # Encode input values to match training encoding
    price_encoded = le_price.transform([price])[0]
    rating_encoded = le_rating.transform([rating])[0]
    reviews_encoded = le_reviews.transform([reviews])[0]
    
    # Predict purchase
    prediction = clf.predict([[price_encoded, rating_encoded, reviews_encoded]])
    return le_purchased.inverse_transform(prediction)[0]

# Example prediction
predicted_purchase = predict_purchase('Affordable', 'High', 'Many')
print("Predicted Purchase:", predicted_purchase)


# In[ ]:




