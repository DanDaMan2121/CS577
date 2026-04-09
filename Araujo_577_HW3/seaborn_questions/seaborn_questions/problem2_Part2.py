# 2. Seaborn. Complete the assignment in the .ipynb file named, “CS677_Seaborn_Questions.”
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')

# print(df.columns)
# we want to show the relationship between days employed
employed = df[df['DAYS_EMPLOYED'] < 0]
employed['DAYS_EMPLOYED'] = -employed['DAYS_EMPLOYED']
x = -employed['DAYS_BIRTH']
y = employed['DAYS_EMPLOYED']
x = x.apply(lambda age_in_years: age_in_years // 365)

sns.histplot(data=df, x=x, binwidth=1, color=sns.xkcd_rgb["light red"])
plt.ylabel('Age in Years')
plt.show()

# incomplete