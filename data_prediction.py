import numpy as np
import os
import sys
#keras
import keras
from keras.models import Sequential, Model
from keras.layers import Convolution1D,LSTM, Dropout, MaxPooling1D, Flatten, Dense, Embedding, Activation, BatchNormalization, GlobalAveragePooling1D, Input, merge, ZeroPadding1D
from keras.preprocessing import sequence
from keras.optimizers import RMSprop, Adam, SGD
from keras.regularizers import l2
#visual output
import matplotlib.pyplot as plt
#custom
from data_import import *

#IMPORTING TRAIN DATASET
train_passagers = clean_passagers([passager(row) for row in import_csv("data/train.csv")])#create all the passager
test_passagers = clean_passagers([passager(row) for row in import_csv("data/test.csv")])#create all the passager

train_x = [] #np.matrix(np.zeros((891,7)))
train_y = []
train_x, train_y = setting_input(train_passagers)

test_x = [] #np.matrix(np.zeros((891,7)))
test_y = []
test_x, test_y = setting_input(test_passagers)

train_x = np.array(train_x)
test_x = np.array(test_x)



#seting the model
print('setting the model')

model = Sequential()
model.add(Dense(32, input_dim=7, activation='relu'))
#model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

#debug
print('model layer##################')
print(model.layers)

print('model layer##################')
print(model.layers[0].get_weights()[1])

#compile
print('compile')
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["acc"])

print('model sumary##################')
print(model.summary())

history = model.fit(train_x, train_y, validation_data=(test_x, test_y), batch_size=8, nb_epoch=10000, shuffle=True, verbose=2)

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

#print(model.layers[0].get_weights()[1])

#evaluate on test data
loss, accuracy = model.evaluate(test_x, test_y)
print("\nLoss: %.2f, Accuracy: %.2f%%" % (loss, accuracy*100))


# make a prediction
ynew = model.predict(test_x)

# show the inputs and predicted outputs
print("X=%s, Predicted=%s" % (test_x[0], ynew[0]))

#[print(np.round(prediction)) for prediction in ynew]

r = csv.reader(open('data/gender_submission.csv')) # Here your csv file
lines = list(r)

for i in range(len(lines)-1) :
  lines[i+1][1] = int(np.round(ynew[i])) #[[int(np.round(prediction)) for prediction in ynew]]

#print(lines)

writer = csv.writer(open('data/output.csv', 'w'))
writer.writerows(lines)
