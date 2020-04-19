from __future__ import absolute_import, division, print_function

import base64
import pandas as pd 
import os
from os.path import realpath, abspath
import numpy as np 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

os.getcwd()
os.listdir(os.getcwd())

class DATASET():
    def __init__(self):
        self.is_data = True
    
    def __image_pass__(self, path, format, test_size ,multiple=True, random_state=None):
        data = []
        files = []
        label_encoder = LabelEncoder()
        if (multiple == True):
            # r=root, d=directories, f = files
            for r, d, f in os.walk(path):
                for file in f:
                    fm = '.' + format
                    if fm in file:
                        files.append(os.path.join(r, file))

            for f in files:
                with open(f, "rb") as imageFile:
                    str = base64.b64encode(imageFile.read())
                    data.append(str)

            encoded_data = label_encoder.fit_transform(data)

            output = pd.DataFrame(encoded_data)           
            y_train, y_test = train_test_split(output, test_size=test_size, random_state=random_state)
            
            return y_train, y_test 
        else:
            with open(path, "rb") as imageFile:
                str = base64.b64encode(imageFile.read())
                data.append(str)    

            encoded_data = label_encoder.fit_transform(data)

            output = pd.DataFrame(encoded_data) 
            y_train, y_test = train_test_split(output, test_size=test_size, random_state=random_state)

            return y_train, y_test  

    def __read_csv__(self, path):
        data_set = pd.read_csv(path, low_memory=False)
        return data_set

    def __read__lb_csv__(self, path, test_size, random_state=None):
        data_set = pd.read_csv(path, low_memory=False)
        x_train , x_test = train_test_split(data_set , test_size=test_size, random_state=random_state)
        return x_train, x_test


    def __obtain_data__csv__el__(self, path, number_features, number_labels, test_size=None, random_state=None):
        if (test_size is not None and random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features:(number_features + number_labels)]
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = test_size, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test
            
        elif (random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , 0:(number_features)]
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test
        
        else:
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features:(number_features + number_labels)]
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = 0)

            return input_x, x_train, x_test, y_train, y_test

    def __obtain_data__csv__fl__(self, path, number_features, number_labels, test_size = None, random_state = None):
        if (test_size is not None and random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , (number_labels+1):(number_features+number_labels+1)]
            input_y = data_set.iloc[ : , 1:(number_labels+1)]
          
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = test_size, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test

        elif (random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , (number_labels+1):(number_features+number_labels+1)]
            input_y = data_set.iloc[ : , 1:(number_labels+1)]
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test
        
        else: 
            data_set = pd.read_csv(path, low_memory=False)
            input_x = data_set.iloc[ : , (number_labels+1):(number_features+number_labels+1)]
            input_y = data_set.iloc[ : , 1:(number_labels+1)]
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = 0)

            return input_x, x_train, x_test, y_train, y_test
    
   