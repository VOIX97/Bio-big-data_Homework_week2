from sklearn.metrics import adjusted_rand_score
from sklearn.cluster import KMeans

def k_means(train_feature,std_label):
    kmeans = KMeans(n_clusters=3).fit(train_feature)
    pre_label = kmeans.labels_
    print("Real label:\n",std_label)
    print("Predict label:\n",pre_label)
    return adjusted_rand_score(std_label,pre_label)