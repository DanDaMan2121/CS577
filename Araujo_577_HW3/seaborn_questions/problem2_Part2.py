# 2. Seaborn. Complete the assignment in the .ipynb file named, “CS677_Seaborn_Questions.”
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')

# we want to show the relationship between days employed
employed = df[df['DAYS_EMPLOYED'] != 365423]

# transform to postive
employed['DAYS_BIRTH'] = -employed['DAYS_BIRTH']
employed['DAYS_EMPLOYED'] = -employed['DAYS_EMPLOYED']

# convert days => years
employed['DAYS_BIRTH'] = employed['DAYS_BIRTH'].apply(lambda age_in_years: age_in_years // 365)

x = employed['DAYS_BIRTH']
y = employed['DAYS_EMPLOYED']

# plot and label
sns.histplot(data=employed, x=x, bins=50, color=sns.xkcd_rgb["light red"])
plt.xlabel('Age in Years')
plt.show()

