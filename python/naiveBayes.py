from sklearn import datasets
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm

digits = datasets.load_digits()

gnb = svm.LinearSVC()

digits['images'].shape = 1797,64

model = gnb.fit(digits['images'][:-300],digits['target'][:-300])

result = model.predict(digits['images'][-300:])

print ( (result == digits['target'][-300:] ).sum())
