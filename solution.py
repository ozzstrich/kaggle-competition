'''
solution.py
'''

import numpy
import math
from keras.models import Sequential
from keras.layers import Dense
numpy.random.seed(14)

class Solution :
    def __init__(self) :
        epochs = 1000 
        
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
        model.compile(loss='mean_squared_error', optimizer='adam')

        # Run model
        model.fit(X, Y, epochs = epochs, batch_size=50)

        # Predict
        predictions = model.predict(X)

        rmse = 0
        for x in range(0, len(predictions)) :
            #print(str(predictions[x]) + " : " + str(Y[x]))
            if Y[x] == 0 : continue
            rmse += math.pow(((Y[x] - predictions[x]) / Y[x]), 2)
        rmse /= len(Y)
        rmse = math.sqrt(rmse)
        print("\nRMSE:", rmse)

Solution()
