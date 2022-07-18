import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Dropout, LSTM
import glob
import numpy as np
import cv2 as cv 
import random


IMG_PATH = 'img/'
training = []
x_train = []
y_train = []
x_test = []
y_test = []
aux_i = 0
for aux_path in range(10):
    images = glob.glob(IMG_PATH + str(aux_path) + '/*.png')
    
    for img in images:
        try:
            print(aux_i)
            aux_i+=1
            img_array = cv.imread(img, cv.COLOR_BGR2RGB)
            new_array = cv.resize(img_array,(48,48))
            print(new_array.shape)
            training.append([new_array, aux_path])
            print(training[0].shape)
        except Exception:
            pass
    
print(len(training))

random.shuffle(training)

for x, y in training:
    x_train.append(x)
    y_train.append(y)

for div in range(len(x_train)//10):
    x_test.append(x_train.pop())
    y_test.append(y_train.pop())

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

print(x_train.shape)
print(y_train.shape)

x_train = x_train/255
x_test = x_test/255

model = Sequential()

model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(x_train,y_train, epochs=8, validation_data=(x_test, y_test))

model.save('./saved_model.h5')
