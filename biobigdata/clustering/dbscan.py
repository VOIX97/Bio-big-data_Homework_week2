from sklearn.cluster import DBSCAN
from sklearn.metrics import adjusted_rand_score
import numpy as np
def dbscan(train_feature,std_label):
    clustering = DBSCAN(eps=30, min_samples=2).fit(train_feature)
    pre_label = clustering.labels_
    print("Real label:\n",np.array([int(item) for item in std_label]))
    print("Predict label:\n",pre_label)
    return adjusted_rand_score(std_label,pre_label)