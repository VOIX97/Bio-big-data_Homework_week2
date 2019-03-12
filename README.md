<<<<<<< HEAD
<<<<<<< HEAD
# Bio-big-data Homework week2
The homework of course Bio-big-data, introducing several algorithms and their results in two datasets.

## Requirements

-  Python>=3.5
-  numpy>=1.14.3
-  scikit-learn>=0.20.0
-  matplotlib>=2.0.2

## Usage

#### Packaging
Git clone this repository, go to the home folder of *Bio-big-data_Homework_week2*, run: 

     python setup.py sdist

Pip installable package will be generated in dist/*.tar.gz
#### Install

Simply run below command:

    pip install ./dist/Bio-big-data-hw2-0.1.0.tar.gz


#### General Options

You can check out the other options available to use with *Ternary* using:

     python -m biobigdata --help

- --method, The processing method: random-forest, svm, knn,
            k-means, dbscan, other (default: None)
- --feature The feature data (default: None)
- --label The label data (default: None)

>Default data was saved in the folder of *data*

#### Example
Generate annotator command:

     python -m biobigdata --method random-forest --feature data/breast_cancer.csv --label data/breast_cancer_class.csv


=======
# Bio-big-data Homework_week2
>>>>>>> 77eea4761f8ca09a3438167a284df378a2b671d5
=======
# Bio-big-data Homework_week2
>>>>>>> 77eea4761f8ca09a3438167a284df378a2b671d5
