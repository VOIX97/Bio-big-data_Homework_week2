from sklearn.svm import NuSVC

def svm(train_feature, train_label):
    clf = NuSVC(kernel='rbf', gamma='scale')
    clf.fit(train_feature, train_label)
    return clf.score(train_feature,train_label)
