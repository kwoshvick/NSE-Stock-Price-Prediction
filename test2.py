from sklearn.externals import joblib
import numpy as np
from flask import Flask,request,jsonify
from sklearn.externals import joblib
import pandas as pd

clf = joblib.load('model.pkl')


a = [19,33,25,29,97,68]
# # a = [20,35,27,13,98,51]
#
# temp = a.reshape((1, -1))
#
# X = np.squeeze(np.asarray(temp))
#
# print(X)

print(clf.predict([a]))

print(clf.predict([[17,	29,	23,	26,	95,	67]]))