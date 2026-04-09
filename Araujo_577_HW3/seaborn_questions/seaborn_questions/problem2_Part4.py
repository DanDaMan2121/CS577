import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')
print(df.columns)


# df.drop('FLAG_MOBIL', inplace=True)
df = df.drop('FLAG_MOBIL', axis=1)
matrix = df.corr(numeric_only=True)
sns.heatmap(data=matrix, cmap='viridis')
plt.show()

# complete