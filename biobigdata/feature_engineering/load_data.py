from sklearn.preprocessing import StandardScaler

def load_train_test(feature_file, label_file):
    """
    load data from train and test files out of the project
    Args:
        feature_file: a string of train data address
        label_file: a string of test data address
    Returns:
        train_feature: none
        train_label: none
    """
    # load data from filex
    train_feature = []
    feature_read = open(feature_file, 'r')
    label_read = open(label_file, 'r')
    train_label = label_read.read().split('\n')[1:-1]
    for line in feature_read.readlines():
        data = line.strip().split(",")
        try:
            _feature = [float(item) for item in data]
            train_feature.append(_feature)
        except:
            continue
    #print(len(train_label),len(train_feature),train_label[-1])
    sc = StandardScaler()
    sc.fit(train_feature)
    train_feature_std = sc.transform(train_feature)
    return train_feature_std, train_label

if __name__ == '__main__':
    featuref = r'E:\SJTU\Homework\bio-big-data\常见机器学习算法实践作业\分类数据\breast_cancer.csv'
    labelf = r'E:\SJTU\Homework\bio-big-data\常见机器学习算法实践作业\分类数据\breast_cancer_class.csv'
    load_train_test(featuref,labelf)

