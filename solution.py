'''
solution.py
'''

import numpy
import math
import os
from keras.models import Sequential, model_from_json
from keras.layers import Dense

numpy.random.seed(14)

def train_model(model, X, Y) :
    # Create model
    model.add(Dense(500, input_dim=15, activation='tanh'))
    model.add(Dense(250, activation='tanh'))
    model.add(Dense(100, activation='tanh'))
    model.add(Dense(1, activation='relu'))

    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')

    # Run model
    model.fit(X, Y, epochs = epochs, batch_size=50)

    # Save model
    my_model = model.to_json()
    file = open("my_model.json", "w")
    file.write(my_model)
    file.close()

    # Save weights
    # FIXME
    weights = model.get_weights()
    file = open("model_weights.txt", "w")
    file.write(str(weights))
    file.close()

def load_model(model) :
    # FIXME
    # Load model file
    file = open("my_model.json", "r")
    contents = file.read()
    file.close()
    model = model_from_json(contents)

    # Set weights
    #file = open("model_weights.txt", "r")
    #contents = file.read()
    #file.close()
    weights = numpy.fromfile("model_weights.txt")
    model.set_weights(weights)

epochs = 1
model = Sequential()
traindata = numpy.loadtxt("train_small.csv", delimiter = ",")
X = traindata[:,0:15]
Y = traindata[:,15]

if not "my_model.json" in os.listdir(".") : train_model(model, X, Y)
else :
    choice = input("Retrain? [y/n] ")
    if choice == "y" : train_model(model, X, Y)
    else : load_model(model)

# Predict
predictions = model.predict(X)

rmse = 0
for x in range(0, len(predictions)) :
    #print(str(predictions[x]) + " : " + str(Y[x]))
    if Y[x] == 0 : continue
    rmse += math.pow(((Y[x] - predictions[x]) / Y[x]), 2)
rmse /= len(Y)
rmse = math.sqrt(rmse)
print("\nTrain RMSE:", rmse)

testdata = numpy.loadtxt("test_small1.csv", delimiter = ",")
Xt = testdata[:,0:15]
Yt = testdata[:,15]
predictionsT = model.predict(Xt)

rmse = 0
for x in range(0, len(predictionsT)) :
    #print(str(predictions[x]) + " : " + str(Y[x]))
    if Yt[x] == 0 : continue
    rmse += math.pow(((Yt[x] - predictionsT[x]) / Yt[x]), 2)
rmse /= len(Yt)
rmse = math.sqrt(rmse)
print("\nTest RMSE:", rmse)"""
