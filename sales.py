'''
sales
'''

import numpy
import math
import os
import keras
from keras.models import Sequential, model_from_json
from keras.layers import Dense

numpy.random.seed(17)

epochs = 10
model = Sequential()
traindata = numpy.loadtxt("train_small.csv", delimiter = ",")
X = traindata[:, 0:15]
Y = traindata[:, 15]
choice = input("Retrain? [y/n]")



def train_model(model, X, Y):
    model.add(Dense(500, input_dim=15, activation='relu'))
    model.add(Dense(250, activation='relu'))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(1, activation='relu'))

    # Compile model
    model.compile(loss = 'mean_squared_error', optimizer = 'adam')

    # Run model
    model.fit(X, Y, epochs = epochs, batch_size = 50)

    # Save Model and weights
    model.save('my_model.h5')
    model.save_weights('my_weights.h5')


def load_model(s):
    model = load_model('my_model.h5')
    model.load_weights("my_weights.h5")

if "my_model.h5" in os.listdir("."):
    load_model(model)
else:
    if choice == "N" or choice=="n":
        load_model(model)
    elif choice == "Y" or "y":
        train_model(model, X, Y)


# Predict
predictions = model.predict(X)

RMSE = 0

# Just for Us
# ============== Prediction for Training Set ==============
for x in range(0, len(predictions)):
    if Y[x] == 0:
        continue
    RMSE += math.pow(((Y[x] - predictions[x]) / Y[x]), 2)
RMSE /= len(Y)
RMSE = math.sqrt(RMSE)
print("\nTrain RMSE:", RMSE)

# ============== Prediction for Test set ==============
testdata = numpy.loadtxt("test_small1.csv", delimiter = ",")
Xt = testdata[:, 0:15]
Yt = testdata[:, 15]
predictionsT = model.predict(Xt)

RMSE = 0
for x in range(0, len(predictionsT)):
    #print(str(predictionsT[x]) + " : " + str(Yt[x]))
    if Yt[x] == 0:
        continue
    RMSE += math.pow(((Yt[x] - predictionsT[x]) / Yt[x]), 2)
RMSE /= len(Yt)
RMSE = math.sqrt(RMSE)
print("\nTest RMSE:", RMSE)
