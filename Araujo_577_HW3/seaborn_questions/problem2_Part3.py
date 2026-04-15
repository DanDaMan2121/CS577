import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')
print(df.columns)

# returns the median
median_income = df['AMT_INCOME_TOTAL'].median()

# filters the dataframe for incomes below the median
bottom_half = df[df['AMT_INCOME_TOTAL'] <= median_income]

# order
order = ['Married', 'Civil marriage', 'Widow', 'Single / not married', 'Separated']

# plot
sns.catplot(data=bottom_half, x='NAME_FAMILY_STATUS', y='AMT_INCOME_TOTAL', hue='FLAG_OWN_REALTY', hue_order=['N', 'Y'], kind='box', order=order)

plt.show()

# complete