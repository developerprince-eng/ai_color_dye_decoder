from __future__ import absolute_import, division, print_function
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.vis_utils import plot_model


def kr_train_DNN_Seq_03():
    model = Sequential()
    model.add(Dense(10, input_dim=6, init='uniform', activation='relu'))
    model.add(Dense(20, init='uniform', activation='relu'))
    model.add(Dense(20, init='uniform', activation='sigmoid'))
    model.add(Dense(1, init='uniform', activation='sigmoid'))
    model.compile(optimizer='sgd', loss='categorical_crossentropy')
                                                                                                                                                                                            
    plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)
if __name__ == "__main__":
    kr_train_DNN_Seq_03()

    