from __future__ import absolute_import, division, print_function

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
    
    def __read_csv__(self, path):
        data_set = pd.read_csv(path, low_memory=False)
        return data_set

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
    
    def __obtain_data__csv__el__lbencode__(self, path, number_features, number_labels, test_size=None, random_state=None):
        if (test_size is not None and random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x1 = label_encoder.fit_transform(ref_input_x.iloc[ : , 0:1])
            temp_x2 = label_encoder.fit_transform(ref_input_x.iloc[ : , 1:2])
            temp_x3 = label_encoder.fit_transform(ref_input_x.iloc[ : , 2:3])
            temp_x4 = label_encoder.fit_transform(ref_input_x.iloc[ : , 3:4])
            temp_x5 = label_encoder.fit_transform(ref_input_x.iloc[ : , 4:5])
            temp_x6 = label_encoder.fit_transform(ref_input_x.iloc[ : , 5:6])
            temp_x7 = label_encoder.fit_transform(ref_input_x.iloc[ : , 6:7])
            temp_x8 = label_encoder.fit_transform(ref_input_x.iloc[ : , 7:8])
            temp_x9 = label_encoder.fit_transform(ref_input_x.iloc[ : , 8:9])
            temp_x10 = label_encoder.fit_transform(ref_input_x.iloc[ : , 9:10])
            temp_x11 = label_encoder.fit_transform(ref_input_x.iloc[ : , 10:11])
            temp_x12 = label_encoder.fit_transform(ref_input_x.iloc[ : , 11:12])
            temp_x13 = label_encoder.fit_transform(ref_input_x.iloc[ : , 12:13])
            temp_x14 = label_encoder.fit_transform(ref_input_x.iloc[ : , 13:14])
            # temp_x15 = label_encoder.fit_transform(ref_input_x.iloc[ : , 14:15])

            temp_x = pd.DataFrame({'x1':temp_x1, 'x2':temp_x2, 'x3':temp_x3, 'x4':temp_x4, 'x5':temp_x5, 'x6':temp_x6, 'x7':temp_x7, 'x8':temp_x8, 'x9':temp_x9, 'x10':temp_x10, 'x11':temp_x11, 'x12':temp_x12, 'x13':temp_x13, 'x14':temp_x14})

            input_x = pd.DataFrame(temp_x)

            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = test_size, random_state = random_state)


            return input_x, x_train, x_test, y_train, y_test
            
        elif (random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x1 = label_encoder.fit_transform(ref_input_x.iloc[ : , 0:1])
            temp_x2 = label_encoder.fit_transform(ref_input_x.iloc[ : , 1:2])
            temp_x3 = label_encoder.fit_transform(ref_input_x.iloc[ : , 2:3])
            temp_x4 = label_encoder.fit_transform(ref_input_x.iloc[ : , 3:4])
            temp_x5 = label_encoder.fit_transform(ref_input_x.iloc[ : , 4:5])
            temp_x6 = label_encoder.fit_transform(ref_input_x.iloc[ : , 5:6])
            temp_x7 = label_encoder.fit_transform(ref_input_x.iloc[ : , 6:7])
            temp_x8 = label_encoder.fit_transform(ref_input_x.iloc[ : , 7:8])
            temp_x9 = label_encoder.fit_transform(ref_input_x.iloc[ : , 8:9])
            temp_x10 = label_encoder.fit_transform(ref_input_x.iloc[ : , 9:10])
            temp_x11 = label_encoder.fit_transform(ref_input_x.iloc[ : , 10:11])
            temp_x12 = label_encoder.fit_transform(ref_input_x.iloc[ : , 11:12])
            temp_x13 = label_encoder.fit_transform(ref_input_x.iloc[ : , 12:13])
            temp_x14 = label_encoder.fit_transform(ref_input_x.iloc[ : , 13:14])
            # temp_x15 = label_encoder.fit_transform(ref_input_x.iloc[ : , 14:15])

            temp_x = pd.DataFrame({'x1':temp_x1, 'x2':temp_x2, 'x3':temp_x3, 'x4':temp_x4, 'x5':temp_x5, 'x6':temp_x6, 'x7':temp_x7, 'x8':temp_x8, 'x9':temp_x9, 'x10':temp_x10, 'x11':temp_x11, 'x12':temp_x12, 'x13':temp_x13, 'x14':temp_x14})

            input_x = pd.DataFrame(temp_x)

            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test

        else:
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x1 = label_encoder.fit_transform(ref_input_x.iloc[ : , 0:1])
            temp_x2 = label_encoder.fit_transform(ref_input_x.iloc[ : , 1:2])
            temp_x3 = label_encoder.fit_transform(ref_input_x.iloc[ : , 2:3])
            temp_x4 = label_encoder.fit_transform(ref_input_x.iloc[ : , 3:4])
            temp_x5 = label_encoder.fit_transform(ref_input_x.iloc[ : , 4:5])
            temp_x6 = label_encoder.fit_transform(ref_input_x.iloc[ : , 5:6])
            temp_x7 = label_encoder.fit_transform(ref_input_x.iloc[ : , 6:7])
            temp_x8 = label_encoder.fit_transform(ref_input_x.iloc[ : , 7:8])
            temp_x9 = label_encoder.fit_transform(ref_input_x.iloc[ : , 8:9])
            temp_x10 = label_encoder.fit_transform(ref_input_x.iloc[ : , 9:10])
            temp_x11 = label_encoder.fit_transform(ref_input_x.iloc[ : , 10:11])
            temp_x12 = label_encoder.fit_transform(ref_input_x.iloc[ : , 11:12])
            temp_x13 = label_encoder.fit_transform(ref_input_x.iloc[ : , 12:13])
            temp_x14 = label_encoder.fit_transform(ref_input_x.iloc[ : , 13:14])
            # temp_x15 = label_encoder.fit_transform(ref_input_x.iloc[ : , 14:15])

            temp_x = pd.DataFrame({'x1':temp_x1, 'x2':temp_x2, 'x3':temp_x3, 'x4':temp_x4, 'x5':temp_x5, 'x6':temp_x6, 'x7':temp_x7, 'x8':temp_x8, 'x9':temp_x9, 'x10':temp_x10, 'x11':temp_x11, 'x12':temp_x12, 'x13':temp_x13, 'x14':temp_x14})

            input_x = pd.DataFrame(temp_x)

            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = random_state)


            return input_x, x_train, x_test, y_train, y_test

    def __obtain_data__csv__fl__lbencode__(self, path, number_features, number_labels, test_size = None, random_state = None):
        if (test_size is not None and random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x = label_encoder.fit_transform(ref_input_x)
            input_x = pd.DataFrame(temp_x)
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = test_size, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test

        elif (random_state is not None):
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x = label_encoder.fit_transform(ref_input_x)
            input_x = pd.DataFrame(temp_x)
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = random_state)

            return input_x, x_train, x_test, y_train, y_test
        
        else: 
            data_set = pd.read_csv(path, low_memory=False)
            ref_input_x = data_set.iloc[ : , 0:(number_features)]
            input_y = data_set.iloc[ : , number_features : (number_features + number_labels)]
            label_encoder = LabelEncoder()
            temp_x = label_encoder.fit_transform(ref_input_x)
            input_x = pd.DataFrame(temp_x)
            
            x_train, x_test, y_train, y_test = train_test_split(input_x, input_y ,test_size = 0.2, random_state = 0)

            return input_x, x_train, x_test, y_train, y_test