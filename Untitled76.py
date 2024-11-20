#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load the dataset
# Ensure 'pizzaprices.csv' is in the same directory
data = pd.read_csv('pizzaprices.csv')

# Inspect the data
print(data.head())

# Prepare the features (X) and target (y)
X = data[['Diameter (inches)']]  # Independent variable
y = data['Price ($)']            # Dependent variable

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Display the model parameters
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

# Predict prices for the given diameters
predicted_prices = model.predict(X)
data['Predicted Price'] = predicted_prices

# Display the dataset with predicted prices
print("\nDataset with Predicted Prices:")
print(data)

# Visualizing the data and regression line
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, predicted_prices, color='red', label='Regression Line')
plt.xlabel('Diameter (inches)')
plt.ylabel('Price ($)')
plt.title('Linear Regression - Pizza Prices')
plt.legend()
plt.show()

# Predict the price for a specific pizza diameter
specific_diameter = 15  # Change this value for different predictions
predicted_price = model.predict([[specific_diameter]])[0]
print(f"The predicted price for a {specific_diameter}-inch pizza is ${predicted_price:.2f}.")


# In[ ]:




