#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Step 1: Prepare the data
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast', 
                'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 
                    'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 
             'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Step 2: Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Step 3: Encode categorical variables
label_encoder_outlook = LabelEncoder()
label_encoder_temperature = LabelEncoder()
label_encoder_play = LabelEncoder()

df['Outlook_encoded'] = label_encoder_outlook.fit_transform(df['Outlook'])
df['Temperature_encoded'] = label_encoder_temperature.fit_transform(df['Temperature'])
df['Play_encoded'] = label_encoder_play.fit_transform(df['Play'])

# Features and target variable
X = df[['Outlook_encoded', 'Temperature_encoded']]
y = df['Play_encoded']

# Step 4: Train the Naive Bayes model
model = CategoricalNB()
model.fit(X, y)

# Step 5: Make a prediction for "Overcast" and "Mild"
outlook_test = label_encoder_outlook.transform(['Overcast'])[0]
temperature_test = label_encoder_temperature.transform(['Mild'])[0]
test_df = pd.DataFrame([[outlook_test, temperature_test]], columns=['Outlook_encoded', 'Temperature_encoded'])

# Predict using the model
prediction = model.predict(test_df)

# Decode the prediction to get the class label
play_prediction = label_encoder_play.inverse_transform(prediction)[0]

print(f"Prediction for Overcast and Mild: {play_prediction}")


# In[ ]:




