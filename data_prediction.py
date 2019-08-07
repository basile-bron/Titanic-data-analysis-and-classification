import numpy as np
import os
import sys
#keras
import keras
from keras.models import Sequential, Model
from keras.layers import Convolution1D,LSTM, Dropout, MaxPooling1D, Flatten, Dense, Embedding, Activation, BatchNormalization, GlobalAveragePooling1D, Input, merge, ZeroPadding1D
from keras.preprocessing import sequence
from keras.optimizers import RMSprop, Adam, SGD
from keras.regularizers import l2
#visual output
import matplotlib.pyplot as plt
#custom
from data_import import *

#IMPORTING TRAIN DATASET
train_passagers = clean_passagers([passager(row) for row in import_csv("data/train.csv")])#create all the passager
test_passagers = clean_passagers([passager(row) for row in import_csv("data/test.csv")])#create all the passager

train_x = [] #np.matrix(np.zeros((891,7)))
train_y = []
train_x, train_y = setting_input(train_passagers)

test_x = [] #np.matrix(np.zeros((891,7)))
test_y = []
test_x, test_y = setting_input(test_passagers)

train_x = np.array(train_x)
test_x = np.array(test_x)

from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble.gradient_boosting import GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import SelectFromModel

parameters = {'bootstrap': False, 'min_samples_leaf': 3, 'n_estimators': 50,
                  'min_samples_split': 10, 'max_features': 'sqrt', 'max_depth': 6}

model = RandomForestClassifier(bootstrap= False, min_samples_leaf= 3, n_estimators= 50,
                  min_samples_split= 10, max_features= 'sqrt', max_depth= 6)
model.fit(train_x, train_y)

pred = model.predict(test_x)
submission = pd.DataFrame({"PassengerId":test_x['PassengerId'],"Survived":pred})
submission.to_csv("titan_random_forest_result.csv",index=False)
