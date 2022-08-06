import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, Flatten
import matplotlib.pyplot as plt

df = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = df.load_data()

""" print(x_train[0])
print(y_train[0])

plt.imshow(x_train[0])
plt.show() """

model = Sequential()

model.add(Flatten())
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dense(128, activation=tf.nn.relu))
model.add(Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'] )
model.fit(x_train, y_train, epochs=5)

model.save('./other_saved_model.h5')
