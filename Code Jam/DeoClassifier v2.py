import numpy as np
import pandas as pd
import time
from sklearn.externals import joblib

from matplotlib.colors import ListedColormap
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import cross_validation
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


h = .02  # step size in the mesh

names = ["Decision Tree", "Linear SVM", "RBF SVM", "AdaBoost"
         #"Random Forest" ,"Naive Bayes",
         #"Linear Discriminant Analysis",
         #"Quadratic Discriminant Analysis"
         ]
classifiers = [
    DecisionTreeClassifier(),
    SVC(kernel="linear", C=0.025, verbose=0),
    SVC(gamma=2, C=1, verbose=0),
    AdaBoostClassifier()
    #RandomForestClassifier(verbose=0),
    #GaussianNB(),
    #LinearDiscriminantAnalysis(),
    #QuadraticDiscriminantAnalysis()
    ]

#import csv

print('Reading File')
print(time.time())
deoFileName = "Deo - IDE - BrandOwner.csv"
data = pd.read_csv(deoFileName)

# select the independent and dependent variables
x = data['Item_Description']
y = data['Brand_Owner']

# Tokenize the Text
print('Tokenizing Text')
print(time.time())

count_vect = CountVectorizer(decode_error='ignore')
x_counts = count_vect.fit_transform(x)

print('Performing TF-IDF Transformation')
print(time.time())
tf_transformer = TfidfTransformer(use_idf=False).fit(x_counts)
x_tf = tf_transformer.transform(x_counts)

tfidf_transformer = TfidfTransformer()
x_tfidf = tfidf_transformer.fit_transform(x_counts)

print('Starting Predictions....')
f = open('results-multiple.csv','w')
for name, clf in zip(names, classifiers):
    print(name)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(x_tfidf, y, test_size=0.4, random_state=1234)
    clf.fit(X_train, y_train)
    score = clf.score(X_test, y_test)
    #predicted = clf.predict(X_test)
    #scores = cross_validation.cross_val_score(clf, X_train, y_train, cv=1)
    print(time.time())
    print("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
    #predicted = cross_validation.cross_val_predict(clf, X_test, y_test, cv=10)
    #print('Accuracy: %s' % (metrics.accuracy_score(y_test, predicted)) )
    f.write(name)
    f.write("Accuracy: %0.2f (+/- %0.2f)" % (score.mean(), score.std() * 2))
    classifierParameterFileNameDump = name + ".pkl"
    joblib.dump(clf, classifierParameterFileNameDump, compress=9)



