# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier
import pickle

# Loading the data
path = 'Data/'
data = pd.read_csv(path+'5.urldata.csv')
print(data.shape)

# Data preprocessing
data = data.drop(['Domain'], axis = 1).copy()
y = data['Label']
X = data.drop('Label',axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

# XGBoost
xgb = XGBClassifier(learning_rate=0.4,max_depth=7,use_label_encoder=False)
xgb.fit(X_train, y_train)
y_test_xgb = xgb.predict(X_test)
y_train_xgb = xgb.predict(X_train)
acc_train_xgb = accuracy_score(y_train,y_train_xgb)
acc_test_xgb = accuracy_score(y_test,y_test_xgb)
print("XGBoost: Accuracy on training Data: {:.3f}".format(acc_train_xgb))
print("XGBoost : Accuracy on test Data: {:.3f}".format(acc_test_xgb))

# Saving the model  
pickle.dump(xgb, open("XGBoostClassifier.pickle.dat", "wb"))
loaded_model = pickle.load(open("XGBoostClassifier.pickle.dat", "rb"))