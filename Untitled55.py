#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

file_path = 'AITASK2.xlsx' 
data = pd.read_excel(file_path, sheet_name='Sheet1')

print("Original Dataset:\n", data)

new_entry = pd.DataFrame({'Gender': ['male'], 'Height': [5.9], 'Weight': [160], 'Foot_Size': [10]})

data = pd.concat([data, new_entry], ignore_index=True)

print("Updated Dataset:\n", data)

le = LabelEncoder()
data['Gender'] = le.fit_transform(data['Gender'])

X = data[['Height', 'Weight', 'Foot_Size']]
y = data['Gender']

clf = DecisionTreeClassifier()
clf.fit(X, y)

new_entry_values = [[5.9, 160, 10]] 
predicted_gender = clf.predict(new_entry_values)

predicted_gender_label = le.inverse_transform(predicted_gender)
print("Predicted Gender for new entry:", predicted_gender_label[0])


# In[ ]:




