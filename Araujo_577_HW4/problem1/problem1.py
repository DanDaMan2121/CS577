import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns

# reading data from a url is as simple using it as a parameter
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
df = pd.read_csv(url, sep=';')

# Q1: Print the first 10 rows of your DataFrame.
print(df.head(10))

# Q2: * Display summary statistics and check for missing values.
df.info()

# Q3: * What is the mean value of Citric Acid content in the dataset?
ca_mean = df['citric acid'].mean()
print(f'The mean for CITRIC ACID is: {ca_mean}')

# Q4: * How many missing values are there?
# 0 missing values

# Q5: * What is the 3rd quartile of Total Sulfur Dioxide content?
third_quartile = df['total sulfur dioxide'].quantile(0.75)
print(f'The third quartile for SULFUR DIOXIDE is: {third_quartile}')

# Q6: * What is the mean quality of wines in the dataset?
mean_quality = df['quality'].mean()
print(f'The mean for QUAILITY of wines is: {mean_quality}')

# Q7: * If `quality=0` describes the worst wine, what is the quality of the best wine in the dataset?
highest_quality = df['quality'].max()
print(f'The HIGHEST QUALITY of wine would be: {highest_quality}')


# PART 2 Data Visualization
plt.figure(1)
sns.scatterplot(df, x='total sulfur dioxide', y='quality')

plt.figure(2)
sns.scatterplot(df, x='pH', y='quality', hue='alcohol')

# plt.show()

# PART 3 Data Preprocessing 

# - Scale the features using the `StandardScaler`standardization technique.
# - Split the data into training and testing sets (e.g., 80% training, 20% testing).

X = df.drop('quality', axis=1)
y = df['quality']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

scaled_X_trian = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)


# - Implement the **ElasticNet regression** algorithm using Scikit-Learn.
# - Explain in your own words what the `alpha` and `l1_ratio` parameters do. You will need to carefully examine the Scikit-Learn Documentation for `ElascitNet` to answer this question.
# - Experiment with different values of `alpha` and `l1_ratio` to find the best combination for your model.

# the 'Alpha' value determines the strength of the penalty applied to the model that punishes outliers.
# a large alpha value may result in the model under fitting which create a model that doest capture the underplaying pattern and results in high error in both the triaing and testing set
# a small alpha value may result in a model over fitting  which results in the model capturing noise and not representing the underlaying pattern
 
# l1_ration controls the balance between Lasso and ridge penalties 
# This value is between 0 and 1 where a l1_ration = 1 would result in a pure lasso model
# and a l1_ratin = 0 would result in a pure ridge penalty


from sklearn.linear_model import ElasticNet

model = ElasticNet(alpha=1.0, l1_ratio=0.1)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(predictions.mean())


from sklearn.linear_model import ElasticNetCV

# cv: number of folds for cross-validation
regr = ElasticNetCV( alphas=[0.01, 0.1, 1.0, 10.0], l1_ratio=[0.1, 0.25, 0.5, 0.75, 0.9], cv=5, random_state=42)
regr.fit(X_train, y_train)

print(f"Best alpha: {regr.alpha_}")
print(f"Best l1_ratio: {regr.l1_ratio_}")

# cross validation help me save a lot of time trying the different combinations of alpha and l1