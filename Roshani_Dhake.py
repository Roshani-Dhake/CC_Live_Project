import pandas as pa
import numpy as nu
import math
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
#from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
import sys

def preprocess_data(stud_cpy):
    stud_cpy.isnull().sum()
    stud_cpy.drop(['Certifications/Achievement/ Research papers'], axis=1, inplace=True)
    stud_cpy.drop(['Link to updated Resume (Google/ One Drive link preferred)'], axis=1, inplace=True)
    stud_cpy.drop("link to Linkedin profile", axis=1, inplace=True)

def analyze_data(stud_cpy):
    stud_cpy.drop(['First Name', 'Last Name', 'City', 'State', 'Zip Code', 'Email Address','DOB [DD/MM/YYYY]','Course Type','Contact Number','Emergency Contact Number','College name','University Name','How Did You Hear About This Internship?','Current Employment Status','Degree','Expected Graduation-year'], axis=1, inplace=True)

def encoding_data(stud_cpy):
    label_encoder = preprocessing.LabelEncoder()
    stud_cpy['Programming Language Known other than Java (one major)'] = label_encoder.fit_transform(
    stud_cpy['Programming Language Known other than Java (one major)'])
    stud_cpy['Areas of interest'] = label_encoder.fit_transform(stud_cpy['Areas of interest'])
    stud_cpy['Have you worked core Java'] = label_encoder.fit_transform(stud_cpy['Have you worked core Java'])
    stud_cpy['Have you worked on MySQL or Oracle database'] = label_encoder.fit_transform(
    stud_cpy['Have you worked on MySQL or Oracle database'])
    stud_cpy['Have you studied OOP Concepts'] = label_encoder.fit_transform(stud_cpy['Have you studied OOP Concepts'])
    gender = pa.get_dummies(stud_cpy['Gender'], drop_first=True)
    year = pa.get_dummies(stud_cpy['Which-year are you studying in?'], drop_first=True)
    major = pa.get_dummies(stud_cpy['Major/Area of Study'], drop_first=True)
    stud_cpy = pa.concat([stud_cpy, gender,year,major], axis=1)
    stud_cpy.drop(['Gender', 'Major/Area of Study', 'Which-year are you studying in?'], axis=1, inplace=True)
    g = pa.get_dummies(stud_cpy['Label'])
    stud_cpy.drop('Label', axis=1, inplace=True)
    stud_cpy = pa.concat([stud_cpy, g], axis=1)
    stud_cpy.drop('ineligible', axis=1, inplace=True)
    X = stud_cpy[['Age', 'CGPA/ percentage', 'Areas of interest', 'Have you worked core Java',
                  'Programming Language Known other than Java (one major)',
                  'Have you worked on MySQL or Oracle database', 'Have you studied OOP Concepts',
                  'Rate your verbal communication skills [1-10]', 'Rate your written communication skills [1-10]', 'Male',
                  'Fourth-year', 'Second-year', 'Third-year', 'Electrical Engineering',
                  'Electronics and Telecommunication']]
    y = stud_cpy["eligible"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train = min_max_scaler.fit_transform(X_train)
    X_test = min_max_scaler.fit_transform(X_test)
    # LOGISTICS REGRESSION
    logmodel = LogisticRegression()
    logmodel.fit(X_train, y_train)
    predictions = logmodel.predict(X_test)
    confusion_matrix(y_test, predictions)
    print(f1_score(y_test, predictions))
    #   DECISION TREE
    #tree_c = DecisionTreeClassifier(max_leaf_nodes=10, random_state=0)
    #tree_c.fit(X_train, y_train)
    #y_p = tree_c.predict(X_test)
    #print(f1_score(y_test, y_p))
    #   SVM
    #classifier_s = svm.SVC(kernel='linear', gamma='auto', C=2)
    #classifier_s.fit(X_train, y_train)
    #y_ps = classifier_s.predict(X_test)
    #print(f1_score(y_test, y_ps))

if __name__ == "__main__":
    stud_cpy = pa.read_csv(sys.argv[1])
    preprocess_data(stud_cpy)
    analyze_data(stud_cpy)
    encoding_data(stud_cpy)
