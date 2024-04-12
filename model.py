import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

data_strong = pd.read_csv('data/IMDB_strong_cleaned.csv')
print(data_strong.head())


X = data_strong.drop("imdb_score", axis=1)
y = data_strong['imdb_score']

# Division des données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)


# gradient boosting
gb = GradientBoostingRegressor(
    n_estimators=100,
    learning_rate=0.1,
    random_state=42)
gb.fit(X_train, y_train)
y_pred_gb = gb.predict(X_test)
print("Gradient Boosting MSE:", mean_squared_error(y_test, y_pred_gb))
print("Gradient Boosting MAE:", mean_absolute_error(y_test, y_pred_gb))
r2_gb = r2_score(y_test, y_pred_gb)
print("Gradient Boosting R²:", r2_gb)

# export du modèle
pickle.dump(gb, open('model.pkl', 'wb'))
