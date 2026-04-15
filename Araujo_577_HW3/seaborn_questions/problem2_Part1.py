# 2. Seaborn. Complete the assignment in the .ipynb file named, “CS677_Seaborn_Questions.”
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')

print(df.columns)

# we want to show the relationship between days employed
employed = df[df['DAYS_EMPLOYED'] < 0]

x = -employed['DAYS_BIRTH']
y = -employed['DAYS_EMPLOYED']

sns.scatterplot(x=x, y=y, alpha=0.01, s=10)
plt.show()


