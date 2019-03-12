from sklearn.preprocessing import StandardScaler

def load_train(feature_file, label_file):
    """
    load data from train file out of the project
    """
    # load data from filex
    with open(label_file,'r') as _train_label:
        train_label = _train_label.readlines()
        std_label = []
        str_list = []
        for item in train_label[1:]:
            if item not in str_list:
                str_list.append(item)
            std_label.append(str(str_list.index(item)))
    train_feature = []
    feature_read = open(feature_file, 'r')
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
    return train_feature_std, std_label

if __name__ == '__main__':
    featuref = r'E:\SJTU\Homework\bio-big-data\常见机器学习算法实践作业\分类数据\breast_cancer.csv'
    labelf = r'E:\SJTU\Homework\bio-big-data\常见机器学习算法实践作业\分类数据\breast_cancer_class.csv'
    load_train_test(featuref,labelf)

