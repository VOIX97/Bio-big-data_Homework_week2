from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from biobigdata.classification.random_forest import *
from biobigdata.clustering import *
from biobigdata.feature_engineering.load_data import load_train_test


def parse_args():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter,
                            conflict_handler='resolve')
    parser.add_argument("-m", "--method",  required=True,
                        choices=['random-forest', 'svm', 'knn', 'k-means',
                                 'dbscan', 'other'],
                        help='The processing method: random-forest, svm, knn, k-means, '
                             ' dbscan, other')
    parser.add_argument("-train", "--train", default=None,
                        help="The train data")
    parser.add_argument("-test", "--test", default=None,
                        help="The test data")
    args = parser.parse_args()
    return args


def main(args):
    if args.method == 'random-forest':
        train_feature, train_label, test_feature, test_label = load_train_test(args.train, args.test)
        accuracy_rate = random_forest(train_feature, train_label, test_feature, test_label)
        print("model random-forest works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'logistic':
        train_feature, train_label, test_feature, test_label = load_train_test(args.train, args.test)
        accuracy_rate = logistic(train_feature, train_label, test_feature, test_label)
        print("model logistic works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'deep-forest':
        train_feature, train_label, test_feature, test_label = load_train_test(args.train, args.test)
        accuracy_rate = deep_forest(train_feature, train_label, test_feature, test_label)
        print("model deep-forest works on the data, the accuracy rate is: ", accuracy_rate)
    if args.method == 'wide-deep':
        print("model wide-deep works on the data, the result is: ")
        wide_deep()
    if args.method == 'xgboost':
        accuracy_rate = xgb_model(args.train, args.test)
        print("model xgboost works on the data, the accuracy rate is: ", accuracy_rate)


if __name__ == "__main__":
    main(parse_args())
