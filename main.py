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



