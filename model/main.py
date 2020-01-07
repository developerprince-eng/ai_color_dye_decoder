from __future__ import absolute_import, division, print_function

from keras.models import Sequential
from keras.layers import Dense
# import tensorflow as tf currently no support for tensorflow manually install(make sure pc  supports tensorlfow)
import pandas as pd 
import os
from os.path import realpath, abspath
import numpy as np 

os.getcwd()
os.listdir(os.getcwd())

class MODEL():
    def __init__(self):
        self.is_model = True

    #Train RNN Classifier
    def kr_train_RNN_Model(self):
        metrics = []
        return metrics
    
    #Train CNN Classifier
    def kr_train_CNN_Model(self):
        metrics = []
        return metrics

    def kr_train_DNN_Seq_01(self,x_dim ,features_train ,features_test, labels_train , labels_test, batch_size):
        # create model
        model = Sequential()
        model.add(Dense(10, input_dim=x_dim, init='uniform', activation='relu'))
        model.add(Dense(60, init='uniform', activation='relu'))
        model.add(Dense(30, init='uniform', activation='sigmoid'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))                                                                                                                                                                                                                       
        # Compile model
        model.compile(loss='mean_squared_error', optimizer='adam',
        metrics=['accuracy'])
        #Model Summary
        model.summary()
        # Fit the model
        model.fit(features_train, labels_train, epochs=10000, batch_size=batch_size, verbose=2)

        score = model.evaluate(features_test, labels_test, verbose=1)
        # round predictions
        accuracy = score[1]
        accuracy = accuracy * 100
    
        return accuracy

    
    def kr_train_DNN_Seq_02(self,x_dim ,features_train ,features_test, labels_train , labels_test, batch_size):
        # create model
        model = Sequential()
        model.add(Dense(9, input_dim=x_dim, init='uniform', activation='relu'))
        model.add(Dense(36, init='uniform', activation='relu'))
        model.add(Dense(36, init='uniform', activation='sigmoid'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))                                                                                                                                                                                                                       
        # Compile model
        model.compile(loss='mean_squared_error', optimizer='adam',
        metrics=['accuracy'])
        # Model Summary
        model.summary()
        # Fit the model
        model.fit(features_train, labels_train, epochs=10000, batch_size=batch_size, verbose=2)

        score = model.evaluate(features_test, labels_test, verbose=1)
        # round predictions
        accuracy = score[1]
        accuracy = accuracy * 100
    
        return accuracy

    def kr_train_DNN_Seq_03(self,x_dim ,features_train ,features_test, labels_train , labels_test, batch_size):
        # create model
        model = Sequential()
        model.add(Dense(10, input_dim=x_dim, init='uniform', activation='relu'))
        model.add(Dense(20, init='uniform', activation='relu'))
        model.add(Dense(20, init='uniform', activation='sigmoid'))
        model.add(Dense(1, init='uniform', activation='sigmoid'))                                                                                                                                                                                                                       
        # Compile model
        model.compile(loss='mean_squared_logarithmic_error', optimizer='adam',
        metrics=['accuracy'])
        # Model Summary
        model.summary()
        # Fit the model
        model.fit(features_train, labels_train, epochs=100, batch_size=batch_size, verbose=2)
        model_yaml = model.to_yaml()
        with open("seq_model.yaml", "w") as yaml_file:
            yaml_file.write(model_yaml)
        # serialize weights to HDF5
        model_json = model.to_json()
        with open("seq_model.json", "w") as json_file:
            json_file.write(model_json)
        model.save_weights("seq_model.h5")
        score = model.evaluate(features_test, labels_test, verbose=1)
        # round predictions
        accuracy = score[1]
        accuracy = accuracy * 100
    
        return accuracy
 
