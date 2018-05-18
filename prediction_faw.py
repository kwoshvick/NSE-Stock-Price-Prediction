import sys
from sklearn.externals import joblib

v_1 = float(sys.argv[1])
v_2 = float(sys.argv[2])
v_3 = float(sys.argv[3])
v_4 = float(sys.argv[4])
v_5 = float(sys.argv[5])
v_6 = float(sys.argv[6])


clf = joblib.load('model.pkl')

a = [19,33,25,29,97,68]


print(clf.predict([[v_1,v_2,v_3,v_4,v_5,v_6]]))

# print(clf.predict([[17,	29,	23,	26,	95,	67]]))