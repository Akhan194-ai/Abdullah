#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Step 1: Define the data
area = np.array([2600, 3000, 3200, 3600, 4000]).reshape(-1, 1)  # Feature (Area)
price = np.array([550000, 565000, 610000, 680000, 725000])      # Target (Price)

# Step 2: Create a linear regression model
model = LinearRegression()

# Step 3: Fit the model to the data
model.fit(area, price)

# Step 4: Use the model to make predictions
area_to_predict = np.array([5000, 8000, 9000]).reshape(-1, 1)  # Areas to predict
predicted_price = model.predict(area_to_predict)

# Output predictions
for area, price in zip(area_to_predict.flatten(), predicted_price):
    print(f"Predicted price of a home with area {area} sqr ft: ${price:,.2f}")

# Optional: Plotting the data and the regression line
plt.scatter(area, price, color='blue', label='Data points')

# To plot the regression line, create a continuous range of area values for prediction
area_range = np.linspace(min(area.flatten()), max(area.flatten()), 100).reshape(-1, 1)  # Fix: flatten area array before applying min/max
plt.plot(area_range, model.predict(area_range), color='red', label='Regression line')

# Plot the predicted points
plt.scatter(area_to_predict, predicted_price, color='green', label='Predictions', zorder=5)

# Labels and legend
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()


# In[1]:





# In[ ]:




