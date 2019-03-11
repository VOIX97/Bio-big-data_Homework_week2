from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,roc_auc_score

def knn(train_feature, train_label):
    final_label = []
    max_score = 0
    for n in range(1,10):
        neigh = KNeighborsClassifier(n_neighbors=n)
        neigh.fit(train_feature, train_label)
        pre_label = neigh.predict_proba(train_feature)
        _pre_label = []
        _pre_score = []
        for item in pre_label:
            if item[0] < item[1]:
                _pre_label.append('0')
            else:
                _pre_label.append('1')
            _pre_score.append(item[1])
        _score = neigh.score(train_feature,train_label)
        if _score > max_score:
            final_label = [item for item in _pre_label]
        print ('AUC when n_neighbor is {}:'.format(str(n)),roc_auc_score(train_label,_pre_score))
        print ('The score of this model when n_neighbor is {}:'.format(str(n)),_score)
    return accuracy_score(train_label, final_label)
