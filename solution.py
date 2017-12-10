'''
solution.py
'''

import numpy
from keras.models import Sequential
from keras.layers import Dense
numpy.random.seed(7)

class Solution :
    def __init__(self) :
        traindata = numpy.loadtxt("train2.csv", delimiter = ",")
        X = traindata[:,0:8]
        Y = traindata[:,8]

        # Create model
        model = Sequential()
        model.add(Dense(12, input_dim=8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='relu'))

        # Compile model
        model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Run model
        model.fit(X, Y, epochs = 150, batch_size=10)

Solution()
