from sklearn import svm
import pickle
a = []
b = []
for i in range(2000):
    a.append(0)
    b.append(1)
X = [a, b]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
filename = 'dummyModel.sav'
pickle.dump(clf, open(filename, 'wb'))