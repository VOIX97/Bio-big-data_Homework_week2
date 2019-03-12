from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from biobigdata.classification.random_forest import random_forest
from biobigdata.classification.svm import svm
from biobigdata.classification.knn import knn
from biobigdata.clustering.k_means import k_means
from biobigdata.clustering.dbscan import dbscan
from biobigdata.feature_engineering.load_data import load_train_test
from biobigdata.feature_engineering.load_cluster_data import load_train
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve,auc
import numpy as np

def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("-m", "--method",  required=True,
                        choices=['random-forest', 'svm', 'knn', 'k-means',
                                 'dbscan', 'other'],
                        help='The processing method: random-forest, svm, knn, k-means, '
                             ' dbscan, other')
    parser.add_argument("-feature", "--feature", default=None,
                        help="The feature data")
    parser.add_argument("-label", "--label", default=None,
                        help="The label data")
    args = parser.parse_args()
    return args


def main(args):
    if args.method == 'random-forest':
        train_feature, train_label= load_train_test(args.feature, args.label)
        accuracy_rate, scores = random_forest(train_feature, train_label)
        print("model random-forest works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'svm':
        train_feature, train_label= load_train_test(args.feature, args.label)
        accuracy_rate, scores = svm(train_feature, train_label)
        print("model svm works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'knn':
        train_feature, train_label= load_train_test(args.feature, args.label)
        accuracy_rate, scores = knn(train_feature, train_label)
        print("model knn works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'k-means':
        train_feature, train_label = load_train(args.feature, args.label)
        accuracy_rate = k_means(train_feature,train_label)
        scores = []
        print("model k-means works on the data, the ari of cluster results is: ", accuracy_rate)
    if args.method == 'dbscan':
        train_feature, train_label = load_train(args.feature, args.label)
        accuracy_rate = dbscan(train_feature,train_label)
        scores = []
        print("model dbscan works on the data, the ari of cluster results is: ", accuracy_rate)
    re_label = train_label
    re_score = scores
    return re_label, re_score, args.method

if __name__ == "__main__":
    label, scores, method = main(parse_args())
    if scores != []:
        fpr, tpr, _ = roc_curve(np.array([int(item) for item in label]), scores)
        roc_auc = auc(fpr,tpr)
        plt.figure()
        lw = 2
        plt.plot(fpr, tpr, color='darkorange',
                 lw=lw, label='ROC curve (auc = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('The ROC curve of algorithm: {}.'.format(method))
        plt.legend(loc="lower right")
        plt.savefig("{}.png".format(method))
        print("ROC curve figure [{}.png] has been saved, please check your folder!".format(method))

