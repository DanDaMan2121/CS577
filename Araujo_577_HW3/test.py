import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("Advertising.csv")
X = df.drop('sales',axis=1) # 3 rows 
y = df['sales'] # 1 col

# cubic becuase we have 3 rows
polynomial_converter = PolynomialFeatures(degree=3,include_bias=False)
poly_features = polynomial_converter.fit_transform(X)

# print(X.shape)
# print(poly_features)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=101)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
print(scaler.fit(X_train))

# print(scaler.mean_)
# print(np.mean(X_train[:, 0]))

# print(scaler.scale_)
# print(np.std(X_train[:, 0]))

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# print(poly_features[:4, 0])
# print(X_train[:4, 0])

from sklearn.linear_model import Ridge

ridge_model = Ridge(alpha=10)
ridge_model.fit(X_train,y_train)
test_predictions = ridge_model.predict(X_test)

from sklearn.metrics import mean_absolute_error, mean_squared_error
MAE = mean_absolute_error(y_test,test_predictions)
MSE = mean_squared_error(y_test,test_predictions)
RMSE = np.sqrt(MSE)

print(MAE)
print(RMSE)

train_predictions = ridge_model.predict(X_train)
MAE = mean_absolute_error(y_train,train_predictions)

from sklearn.linear_model import RidgeCV

# from sklearn.metrics import fbeta_score, Scorer
# sklearn.metrics.Scorer.keys()
from sklearn.metrics import get_scorer_names
print(get_scorer_names())

# Choosing a scoring: https://scikit-learn.org/stable/modules/model_evaluation.
# ↪html
# Negative RMSE so all metrics follow convention "Higher is better"
# See all options: get_scorer_names
# ridge_cv_model = RidgeCV(alphas=(0.1, 1.0, 10.
# ↪0),scoring='neg_mean_absolute_error')
ridge_cv_model = RidgeCV(alphas=(0.1, 1.0, 10.0),scoring='neg_mean_squared_error')
# ridge_cv_model.alphas_
ridge_cv_model.fit(X_train,y_train)
test_predictions = ridge_cv_model.predict(X_test)

MAE = mean_absolute_error(y_test,test_predictions)
MSE = mean_squared_error(y_test,test_predictions)
RMSE = np.sqrt(MSE)

print(MAE, RMSE)

train_predictions = ridge_cv_model.predict(X_train)
MAE_training = mean_absolute_error(y_train,train_predictions)
print(MAE_training)

print(ridge_cv_model.coef_)