from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from biobigdata.classification.random_forest import random_forest
from biobigdata.classification.svm import svm
from biobigdata.classification.knn import knn
from biobigdata.clustering.k_means import k_means
from biobigdata.clustering.dbscan import dbscan
from biobigdata.feature_engineering.load_data import load_train_test
from biobigdata.feature_engineering.load_cluster_data import load_train

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
        accuracy_rate = random_forest(train_feature, train_label)
        print("model random-forest works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'svm':
        train_feature, train_label= load_train_test(args.feature, args.label)
        accuracy_rate = svm(train_feature, train_label)
        print("model svm works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'knn':
        train_feature, train_label= load_train_test(args.feature, args.label)
        accuracy_rate = knn(train_feature, train_label)
        print("model knn works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'k-means':
        train_feature = load_train(args.feature)
        accuracy_rate = k_means(train_feature)
        print("model k-means works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'dbscan':
        train_feature = load_train(args.feature)
        accuracy_rate = dbscan(train_feature)
        print("model dbscan works on the data, the accuracy rate is: ", accuracy_rate)


if __name__ == "__main__":
    main(parse_args())
