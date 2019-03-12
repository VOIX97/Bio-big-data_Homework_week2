from sklearn.svm import NuSVC
<<<<<<< HEAD
from sklearn.metrics import roc_auc_score
=======
from sklearn.metrics import accuracy_score
>>>>>>> 77eea4761f8ca09a3438167a284df378a2b671d5

def svm(train_feature, train_label):
    clf = NuSVC(kernel='rbf', gamma='scale', probability=True)
    clf.fit(train_feature, train_label)
<<<<<<< HEAD
    pre_score = clf.predict_proba(train_feature)
    _pre_label = []
    _pre_score = []
    for item in pre_score:
        if item[0] > item[1]:
            _pre_label.append('0')
        else:
            _pre_label.append('1')
        _pre_score.append(item[1])
    print ('The auc is: {}'.format(roc_auc_score(train_label,_pre_score)))
    print ('The score is: {}'.format(clf.score(train_feature,train_label)))
    return clf.score(train_feature,train_label)
=======
    _pre_label = clf.predict_proba(train_feature)
    _score = clf.score(train_feature,train_label)
    return accuracy_score(train_label, _pre_label)
>>>>>>> 77eea4761f8ca09a3438167a284df378a2b671d5
