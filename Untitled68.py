#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Step 1: Load data from Excel file
# Make sure 'homeprices.xlsx' is in the same directory or provide the full path
df = pd.read_excel('lab.csv')

# Step 2: Check the structure of the data
print(df.head())

# Assuming the columns are named 'Area' and 'Price', you can change these names based on your Excel file structure
X = df['Area'].values.reshape(-1, 1)  # Area (square feet)
y = df['Price'].values  # Price (in dollars)

# Step 3: Train the Linear Regression Model
model = LinearRegression()
model.fit(X, y)

# Step 4: Make Predictions for new areas (e.g., 2500, 3500, 4500 sqft)
areas_to_predict = np.array([2500, 3500, 4500]).reshape(-1, 1)
predicted_prices = model.predict(areas_to_predict)

# Display the predictions
for area, price in zip(areas_to_predict, predicted_prices):
    print(f"Predicted price for a house with area {area[0]} sqft: ${price:,.2f}")

# Step 5: Visualize the data and the regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Linear Regression Line')
plt.xlabel('Area (sqft)')
plt.ylabel('Price ($)')
plt.title('Linear Regression for Predicting Home Prices')
plt.legend()
plt.show()

# Optionally, you can print the slope (coefficient) and intercept
print(f"Slope (coefficient): {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")


# In[5]:


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
area_range = np.linspace(min(area), max(area), 100).reshape(-1, 1)  # 100 values between min and max area
plt.plot(area_range, model.predict(area_range), color='red', label='Regression line')

# Plot the predicted points
plt.scatter(area_to_predict, predicted_price, color='green', label='Predictions', zorder=5)

# Labels and legend
plt.xlabel('Area (sq ft)')
plt.ylabel('Price ($)')
plt.legend()
plt.show()


# In[ ]:




