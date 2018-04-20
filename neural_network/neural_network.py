import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation

from sklearn.neural_network import MLPRegressor



df = pd.read_csv('../SCOM.csv')

df_close = df[[3]]

forecast_out = int(30) # predicting 30 days into future


df['Prediction'] = df_close.shift(-forecast_out) #  label column with data shifted 30 units up

# print(df.tail())

X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)



X_forecast = X[-forecast_out:] # set X_forecast equal to last 30
X = X[:-forecast_out] # remove last 30 from X


y = np.array(df['Prediction'])
y = y[:-forecast_out]



X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.3)

# Training
clf = MLPRegressor()
# clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                     hidden_layer_sizes=(5, 2), random_state=1)
clf.fit(X_train,y_train)
# Testing
confidence = clf.score(X_test, y_test)
print("confidence: ", confidence)


forecast_prediction = clf.predict(X_forecast)
print(forecast_prediction)
