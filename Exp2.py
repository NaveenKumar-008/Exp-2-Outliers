import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("bhp.csv")
Q1 = df['price_per_sqft'].quantile(0.25)
Q3 = df['price_per_sqft'].quantile(0.75)
IQR = Q3 - Q1
lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
df_iqr = df[(df['price_per_sqft'] >= lower_limit) & (df['price_per_sqft'] <=
upper_limit)]
print("New data:",df_iqr)
from scipy.stats import zscore
df_z = df_iqr[(zscore(df_iqr['price_per_sqft']) < 3)]
print("Result",df_z) 


import pandas as pd
from google.colab import files
uploaded = files.upload()
df = pd.read_csv("height_weight.csv")
print(df.head())
Q1 = df['weight'].quantile(0.25)
Q3 = df['weight'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['weight'] < lower_bound) | (df['weight'] >
upper_bound)]
print("Weight Outliers",outliers)
Q1 = df['height'].quantile(0.25)
Q3 = df['height'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers = df[(df['height'] < lower_bound) | (df['height'] >
upper_bound)]
print("Height outliers",outliers)
