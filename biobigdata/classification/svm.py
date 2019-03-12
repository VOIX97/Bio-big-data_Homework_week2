from sklearn.svm import NuSVC
from sklearn.metrics import accuracy_score

def svm(train_feature, train_label):
    clf = NuSVC(kernel='rbf', gamma='scale', probability=True)
    clf.fit(train_feature, train_label)
    _pre_label = clf.predict_proba(train_feature)
    _score = clf.score(train_feature,train_label)
    return accuracy_score(train_label, _pre_label)
