import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

df = pd.read_csv('application_record.csv')
print(df.columns)

# drop flag_mobil
df = df.drop('FLAG_MOBIL', axis=1)

# create heat map matrix
matrix = df.corr(numeric_only=True)

sns.heatmap(data=matrix, cmap='viridis')
plt.show()

# complete