
from sklearn.externals import joblib




clf = joblib.load('model.pkl')


a = [19,33,25,29,97,68]


print(clf.predict([a]))

print(clf.predict([[17,	29,	23,	26,	95,	67]]))