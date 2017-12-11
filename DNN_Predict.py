import numpy
import math
import keras
from keras.models import Sequential, model_from_json, load_model
from keras.layers import Dense


testdata = numpy.loadtxt("test_big.csv", delimiter = ",")
X = testdata[:,1:15]
ID=testdata[:,0]
model = load_model('model.h5')
model.load_weights("weights.h5")
file=open("KagglePredictions.csv","w+")
predictions = model.predict(X)
#trueSales= testdata[:,15]
file.write("storeID, salesPredicition\n")
for i,p in zip(ID,predictions):
	line=str(i)+","+str(int(p))+"\n"
	file.write(line)



