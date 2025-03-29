import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('new.csv')
print(df.head())
df.shape

#data preprocessing
df.info()
print (df.describe().T)
#to check null values in datatset
for col in df.columns:
    temp = df[col].isnull().sum()
    if temp > 0:
        print(f'Column {col} contains {temp} null values.')



df = df.dropna()
print("Total missing values are:", len(df))


#To find the total number of unique values in each column
print (df.nunique())
#we can convert Dt_Customer into 3 columns i.e. day, month, year. 
parts = df["Dt_Customer"].str.split("-", n=3, expand=True)
df["day"] = parts[0].astype('int')
df["month"] = parts[1].astype('int')
df["year"] = parts[2].astype('int')
#drop features like Z_CostContact, Z_Revenue, Dt_Customer.
df.drop(['Z_CostContact', 'Z_Revenue', 'Dt_Customer'],
        axis=1,
        inplace=True)

#data visualization and analysis
# Identify categorical (object) and numerical (float) columns
floats, objects = [], []
for col in df.columns:
    if df[col].dtype == object:
        objects.append(col)
    elif df[col].dtype == float or df[col].dtype == int:  # Include int columns too
        floats.append(col)

print(objects)
print(floats)

plt.subplots(figsize=(15, 10))
for i, col in enumerate(objects):
    plt.subplot(2, 2, i + 1)
    sb.countplot(df[col])
plt.show()






