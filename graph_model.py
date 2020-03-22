<<<<<<< HEAD
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

    
=======
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import plot_model

def main():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='softmax'))                                                                                                                                                                                                                        
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam',
    metrics=['accuracy'])
    #Model Summary
    model.summary()
    plot_model(model, to_file='model.png')

if __name__ == "__main__":
    main()
>>>>>>> 4d7940c95782f223cf7a06f49042aec155d51bb8
