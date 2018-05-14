from sklearn.externals import joblib
import numpy as np

clf = joblib.load('model.pkl')

a = np.array([19,33,25,29,97,68])
# a = [20,35,27,13,98,51]

temp = a.reshape((1, -1))

X = np.squeeze(np.asarray(temp))

print(X)

clf.predict(X)