from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,roc_auc_score

def knn(train_feature, train_label):
    final_label = []
    for n in range(1,10):
        neigh = KNeighborsClassifier(n_neighbors=n)
        neigh.fit(train_feature, train_label)
        pre_label = neigh.predict_proba(train_feature)
        _pre_label = []
        _pre_score = [item[1] for item in pre_label]
        for item in pre_label:
            if item[0] > item[1]:
                _pre_label.append('0')
            else:
                _pre_label.append('1')
        _score = neigh.score(train_feature,train_label)
        final_label = [item for item in _pre_label]
        _accuracy = accuracy_score(train_label, final_label)
        print ('AUC when n_neighbor is {}:'.format(str(n)),roc_auc_score(train_label,_pre_score))
        print ('The score of this model when n_neighbor is {}:'.format(str(n)),_score)
        print ('The accuracy of this model when n_neighbor is {}:'.format(str(n)),_accuracy)
    return accuracy_score(train_label, final_label)
