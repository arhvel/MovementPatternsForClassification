#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon March 7 14:00:10 2022

@author: adeyem01
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier

import pandas as pd
import numpy as np
from numpy import mean
from numpy import std
from collections import defaultdict

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_validate, cross_val_score
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score

from itertools import chain

# lccSPM
data = pd.read_csv('ResultsMatrix_LCCspm_patternbased.csv')
data_predictors = data.drop('Position',1)
data_predictors = data_predictors.drop('ath_id',1)
data_predictors = data_predictors.drop('Fixture',1)
data_target = data['Position']

# SMP
SMPdata = pd.read_csv('ResultsMatrix_SMP_patternbased.csv')
SMPdata_predictors = SMPdata.drop('Position',1)
SMPdata_predictors = SMPdata_predictors.drop('ath_id',1)
SMPdata_predictors = SMPdata_predictors.drop('Fixture',1)
SMPdata_target = SMPdata['Position']

# AprioriClose 
APRdata = pd.read_csv('ResultsMatrix_APR_patternbased.csv')

APRdata_predictors = APRdata.drop('Position',1)
APRdata_predictors = APRdata_predictors.drop('ath_id',1)
APRdata_predictors = APRdata_predictors.drop('Fixture',1)
APRdata_target = APRdata['Position']

# Model Dev

## Model Initialization
LOGREG = LogisticRegression(penalty='l1', solver='liblinear')
RF = RandomForestClassifier(random_state=1)
NB = GaussianNB()
DT = tree.DecisionTreeClassifier()
MLP = MLPClassifier(random_state = 5, max_iter=300)

models= [DT, NB, RF, LOGREG, MLP]
#models= [DT]

## Cross Validation Techniques
cv= KFold(n_splits=10, random_state=10, shuffle=True )

#Model building and evaluation
scoring = {'accuracy' : make_scorer(accuracy_score),'precision' : make_scorer(precision_score, pos_label=None, average='macro'),'recall' : make_scorer(recall_score, pos_label=None, average='macro'), 'f1_score' : make_scorer(f1_score, pos_label=None, average='macro')}

results = []
print('========= LCCspm =========')
for model in models:
    scores = cross_validate(model, data_predictors, data_target, scoring= scoring, cv=cv, n_jobs=1)
    
    accuracy = mean(scores['test_accuracy']*100)
    accuracy_SD = std(scores['test_accuracy'])
    precision = mean(scores['test_precision'])
    recall = mean(scores['test_recall'])
    f1 = mean(scores['test_f1_score'])
    _com = (str(model), accuracy, accuracy_SD, precision, recall,f1)
    results.append(_com)
    
    print('Performance results for %s:' %(str(model)))
    print('Accuracy : ',accuracy,'with a standard deviation of ',accuracy_SD, 'Precision: ', precision, ' Recall: ', recall, 'and F1-score', f1)
    print('==============================================================================================================')

    
results_SMP = []
print('========= SMP =========')
for model in models:
    scores_SMP = cross_validate(model, SMPdata_predictors, SMPdata_target, scoring=scoring, cv=cv, n_jobs=1)
    
    
    accuracy = mean(scores_SMP['test_accuracy']*100)
    accuracy_SD = std(scores_SMP['test_accuracy'])
    precision = mean(scores_SMP['test_precision'])
    recall = mean(scores_SMP['test_recall'])
    f1 = mean(scores_SMP['test_f1_score'])
    _com = (str(model), accuracy, accuracy_SD, precision, recall,f1)
    results_SMP.append(_com)
    
    print('Performance results for %s:' %(str(model)))
    print('Accuracy : ',accuracy,'with a standard deviation of ',accuracy_SD, 'Precision: ', precision, ' Recall: ', recall, 'and F1-score', f1)
    print('==============================================================================================================')


results_APR = []
print('========= APR =========')
for model in models:
    scores_APR = cross_validate(model, APRdata_predictors, APRdata_target, scoring=scoring, cv=cv, n_jobs=1)
    
    accuracy = mean(scores_APR['test_accuracy']*100)
    accuracy_SD = std(scores_APR['test_accuracy'])
    precision = mean(scores_APR['test_precision'])
    recall = mean(scores_APR['test_recall'])
    f1 = mean(scores_APR['test_f1_score'])
    _com = (str(model), accuracy, accuracy_SD, precision, recall,f1)
    results_APR.append(_com)
    
    print('Performance results for %s:' %(str(model)))
    print('Accuracy : ',accuracy,'with a standard deviation of ',accuracy_SD, 'Precision: ', precision, ' Recall: ', recall, 'and F1-score', f1)
    print('==============================================================================================================')

resultFrames = []
columns = ['Classifier','Accuracy','SD', 'Precision', 'Recall', 'F1_Score']
LCC = pd.DataFrame(results, columns = columns)
LCC['Method']= 'LCCspm'
resultFrames.append(LCC)

SMP = pd.DataFrame(results_SMP, columns = columns)
SMP['Method']= 'SMP'
resultFrames.append(SMP)

AprioriClose = pd.DataFrame(results_APR, columns = columns)
AprioriClose['Method']= 'AprioriClose'
resultFrames.append(AprioriClose)

resultFrames = pd.concat(resultFrames).reset_index(drop=True)
resultFrames.to_csv('ClassificationResults.csv', index=False)

## Featuring Importance
class_LCC = cross_validate(LOGREG, data_predictors, data_target, scoring='accuracy', cv=cv, n_jobs=1, return_estimator =True)
FI_lcc = []
for idx,estimator in enumerate(class_LCC['estimator']):
    print("Features sorted by their score for estimator {}:".format(idx))
    variables = list(data_predictors.columns)
    feature_importances = pd.DataFrame(estimator.coef_, columns=variables)
    feature_importances = feature_importances.T
    feature_importances.columns = ["Importance"]
    FI_lcc.append(feature_importances)
# collate the importance score of each pattern to a list
PatternsImportances = defaultdict(list)
for i in range(len(FI_lcc)):
    data = FI_lcc[i]
    data = data.reset_index()
    data.rename(columns = {'index':'Patterns'}, inplace = True)
    diction = list(tuple(zip(data.Patterns, data.Importance)))
    # append to the dictionary
    for key, value in diction:
        PatternsImportances[key].append(value)
# Calcualte the mean importance score per pattern
PattMeanImportance = []
for key, values in PatternsImportances.items():
    mmn = mean(values)
    collate = (key, mmn)
    PattMeanImportance.append(collate)  
PattMeanImportance_lcc = pd.DataFrame(PattMeanImportance, columns = ['Patterns', 'Importance'] ).sort_values('Importance', ascending=False)
PattMeanImportance_lcc_patterns =  PattMeanImportance_lcc.iloc[:20]


class_SMP = cross_validate(LOGREG, SMPdata_predictors, SMPdata_target, scoring='accuracy', cv=cv, n_jobs=1, return_estimator =True)
FI_smp = []
for idx,estimator in enumerate(class_SMP['estimator']):
    print("Features sorted by their score for estimator {}:".format(idx))
    variables = list(SMPdata_predictors.columns)
    feature_importances = pd.DataFrame(estimator.coef_, columns=variables)
    feature_importances = feature_importances.T
    feature_importances.columns = ["Importance"]
    FI_smp.append(feature_importances)
PatternsImportances = defaultdict(list)
for i in range(len(FI_smp)):
    data = FI_smp[i]
    data = data.reset_index()
    data.rename(columns = {'index':'Patterns'}, inplace = True)
    diction = list(tuple(zip(data.Patterns, data.Importance)))
    # append to the dictionary
    for key, value in diction:
        PatternsImportances[key].append(value)
PattMeanImportance = []
for key, values in PatternsImportances.items():
    mmn = mean(values)
    collate = (key, mmn)
    PattMeanImportance.append(collate)  
PattMeanImportance_SMP = pd.DataFrame(PattMeanImportance, columns = ['Patterns', 'Importance'] ).sort_values('Importance', ascending=False)
PattMeanImportance_SMP_patterns =  PattMeanImportance_SMP.iloc[:20]


class_APR = cross_validate(LOGREG, APRdata_predictors, APRdata_target, scoring='accuracy', cv=cv, n_jobs=1, return_estimator =True)
FI_apr = []
for idx,estimator in enumerate(class_APR['estimator']):
    print("Features sorted by their score for estimator {}:".format(idx))
    variables = list(APRdata_predictors.columns)
    feature_importances = pd.DataFrame(estimator.coef_, columns=variables)
    feature_importances = feature_importances.T
    feature_importances.columns = ["Importance"]
    FI_apr.append(feature_importances)
PatternsImportances = defaultdict(list)
for i in range(len(FI_apr)):
    data = FI_apr[i]
    data = data.reset_index()
    data.rename(columns = {'index':'Patterns'}, inplace = True)
    diction = list(tuple(zip(data.Patterns, data.Importance))) 
    # append to the dictionary
    for key, value in diction:
        PatternsImportances[key].append(value)
PattMeanImportance = []
for key, values in PatternsImportances.items():
    mmn = mean(values)
    collate = (key, mmn)
    PattMeanImportance.append(collate)  
PattMeanImportance_APR = pd.DataFrame(PattMeanImportance, columns = ['Patterns', 'Importance'] ).sort_values('Importance', ascending=False) 
PattMeanImportance_APR_patterns =  PattMeanImportance_APR.iloc[:20]