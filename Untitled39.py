#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Step 1: Prepare the dataset
data = {
    'age': ['youth', 'youth', 'middle_aged', 'senior', 'senior', 'senior', 
            'middle_aged', 'youth', 'youth', 'senior', 'youth', 'middle_aged', 
            'middle_aged', 'senior'],
    'income': ['high', 'high', 'high', 'medium', 'low', 'low', 
               'low', 'medium', 'low', 'medium', 'medium', 'medium', 
               'high', 'medium'],
    'student': ['no', 'no', 'no', 'no', 'yes', 'yes', 
                'yes', 'no', 'yes', 'yes', 'yes', 'no', 
                'yes', 'no'],
    'credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 
                      'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 
                      'fair', 'excellent'],
    'buys_computer': ['no', 'no', 'yes', 'yes', 'yes', 'no', 
                      'yes', 'no', 'yes', 'yes', 'yes', 'yes', 
                      'yes', 'no']
}

# Step 2: Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Step 3: Encode categorical variables
label_encoder_age = LabelEncoder()
label_encoder_income = LabelEncoder()
label_encoder_student = LabelEncoder()
label_encoder_credit_rating = LabelEncoder()
label_encoder_buys_computer = LabelEncoder()

df['age_encoded'] = label_encoder_age.fit_transform(df['age'])
df['income_encoded'] = label_encoder_income.fit_transform(df['income'])
df['student_encoded'] = label_encoder_student.fit_transform(df['student'])
df['credit_rating_encoded'] = label_encoder_credit_rating.fit_transform(df['credit_rating'])
df['buys_computer_encoded'] = label_encoder_buys_computer.fit_transform(df['buys_computer'])

# Features and target variable
X = df[['age_encoded', 'income_encoded', 'student_encoded', 'credit_rating_encoded']]
y = df['buys_computer_encoded']

# Step 4: Train the Naive Bayes model
model = CategoricalNB()
model.fit(X, y)

# Step 5: Make a prediction for "youth", "medium", "yes", "fair"
age_test = label_encoder_age.transform(['youth'])[0]
income_test = label_encoder_income.transform(['medium'])[0]
student_test = label_encoder_student.transform(['yes'])[0]
credit_rating_test = label_encoder_credit_rating.transform(['fair'])[0]

# Create DataFrame for the test data with column names
test_df = pd.DataFrame([[age_test, income_test, student_test, credit_rating_test]], 
                       columns=['age_encoded', 'income_encoded', 'student_encoded', 'credit_rating_encoded'])

# Predict using the model
prediction = model.predict(test_df)

# Decode the prediction to get the class label
buys_computer_prediction = label_encoder_buys_computer.inverse_transform(prediction)[0]

print(f"Prediction for youth, medium, yes, fair: {buys_computer_prediction}")


# In[ ]:




