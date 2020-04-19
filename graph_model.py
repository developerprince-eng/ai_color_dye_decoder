from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.utils import plot_model

def main():
    model = Sequential()
    model.add(Dense(1, input_dim=1, init='uniform', activation='relu'))
    model.add(Dense(4, init='uniform', activation='relu'))
    model.add(Dense(8, init='uniform', activation='sigmoid'))
    model.add(Dense(5, init='uniform', activation='sigmoid'))                                                                                                                                                                                                                       
    # Compile model
    model.compile(loss='binary_crossentropy', optimizer='adam',
    metrics=['accuracy'])
    #Model Summary
    model.summary()
    plot_model(model, to_file='model.png')

if __name__ == "__main__":
    main()
