'''
solution.py
'''

import numpy
import keras
import math
from keras.models import Sequential
from keras.layers import Dense
numpy.random.seed(7)

class Solution :
    def __init__(self) :
        traindata = numpy.loadtxt("train_small.csv", delimiter = ",")
        X = traindata[:,0:15]
        Y = traindata[:,15]

        # Create model
        model = Sequential()
        model.add(Dense(500, input_dim=15, activation='tanh'))
        model.add(Dense(250, activation='tanh'))
        model.add(Dense(100, activation='tanh'))
        model.add(Dense(1, activation='relu'))

        # Compile model
        #keras.optimizers.Adam(lr=0.5)
        model.compile(loss='mean_squared_error', optimizer='adam')

        # Run model
        model.fit(X, Y, epochs = 50, batch_size=50)

        # Predict
        predictions = model.predict(X)

        #RMSE NOT WORKING!!
        rmse = 0
        for x in range(0, len(predictions)) :
            print(str(predictions[x]) + " : " + str(Y[x]))
            rmse += math.pow((Y[x] - predictions[x]) / Y[x], 2)
        rmse = math.sqrt(rmse / len(predictions))
        print("RMSE:", rmse)

Solution()
