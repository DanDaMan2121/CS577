# 3. Seaborn. Complete the assignment in the .ipynb file named, “CS677_California_Housing_HOMEWORK.”
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

# df = pd.read_csv('Ocean_Proximity.csv')
# print(df.columns)

from sklearn.datasets import fetch_california_housing

# This method is used to download and load california housing dataset
# as_frame = True is an option that returns a Pandas object instead of a numpy array
# 2 other data sets are of penguins and blood transfusions
california_housing = fetch_california_housing(as_frame=True)
df = california_housing.frame

# TASK 2

# 1
print(df.head(3))
print("=======")

# 2
print(df)
print(f'regression label: {df.columns[-1]}')
print("=======")

# 3
print(f"number of null values: {df.isnull().sum().sum()}")
print(f'number of non-null values: {df.notna().sum().sum()}')
print('=======')
# 4
unique_latitude = df['Latitude'].unique()
print(f"number of unique Latitude values: {len(unique_latitude)}")

unique_longitude = df['Longitude'].unique()
print(f'number of unique Longitude values: {len(unique_longitude)}')

print('=======')

# 5
col = pd.read_csv('Ocean_Proximity.csv')
df['ocean_proximity'] = col['ocean_proximity']
print(df.head(3))

keys = df['ocean_proximity'].unique()
values = range(len(keys))
proximity_map = {keys[i]:values[i] for i in range(len(keys))}

# df['ocean_proximity'] = df['ocean_proximity'].replace(proximity_map)
print(df.head(3))
print('=======')

# 6
sns.barplot(data=df, x='ocean_proximity', y='MedHouseVal')

# 7
sns.jointplot(x=df['MedInc'], y=df['MedHouseVal'], kind='hex', color='orange')

# 8
df['ocean_proximity'] = df['ocean_proximity'].replace(proximity_map)
numeric_df = df.select_dtypes(include=['number'])
X = numeric_df.drop('MedHouseVal', axis=1)
y = numeric_df['MedHouseVal']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Create the scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6, edgecolor='w')

plt.xlabel('Predicted house prices', fontsize=12)
plt.ylabel('MedHouseVal', fontsize=12)
plt.ylim(0, 5.1)
plt.show()

