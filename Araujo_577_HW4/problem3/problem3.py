import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("hearing_test.csv")

# Read the given dataset into a DataFrame and display the first 6 rows.
print(df.head(6))

## Exploratory Data Analysis (EDA)

# 1. How many `non-null` entries does the Dataset have?
df.info()
print('1500 non-null entries')
# 2. What is the mean age of the participants in the study?
mean_age = df['age'].mean()
print(f'The mean AGE is: {mean_age}')
# 3. What is the IQR of the `physical_score` feature?
physical_IQR = df['physical_score'].quantile(0.75) - df['physical_score'].quantile(0.25)
print(f'physical IQR: {physical_IQR}')
# 4. How old is the oldest participant?
oldest = df['age'].max()
print(f'Oldest participant: {oldest}')
# 5. What Pandas method will give you the number of `1`s and `0`s in the label? What are the values?
print(df['test_result'].value_counts())




from mpl_toolkits.mplot3d import Axes3D 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['age'],df['physical_score'],df['test_result'],c=df['test_result'])
ax.set_xlabel('Age')
ax.set_ylabel('Physical Score')
# ax.set_zlabel('Pass/Not Pass')
plt.show()

X = df.drop('test_result', axis=1)
y = df['test_result']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LogisticRegression()
model.fit(X_train_scaled, y_train)

from sklearn.pipeline import Pipeline

# Combine scaling and modeling into one object
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logistic', LogisticRegression())
])

# Now you just fit and predict with the pipeline
pipeline.fit(X_train, y_train)
accuracy = pipeline.score(X_test, y_test)

print(f"accuracy {accuracy}")