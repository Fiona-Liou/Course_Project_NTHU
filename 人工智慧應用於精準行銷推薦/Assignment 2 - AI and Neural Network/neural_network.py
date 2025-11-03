import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import numpy as np
unique, counts = np.unique(y_train, return_counts=True)
print(np.asarray((unique, counts)))

x_train_normalized = x_train / 255
x_test_normalized = x_test / 255
print(x_train_normalized[-2])

from tensorflow.keras.utils import to_categorical

y_train_10 = to_categorical(y_train, num_classes=10)
y_test_10  = to_categorical(y_test,  num_classes=10)
print(y_train_10.shape)
print(y_train_10[0])

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation

model_dnn = Sequential([
  Dense(units=128, input_shape=(784,), activation='relu'),
  Dense(units=64, activation='relu'),
  Dense(units=32, activation='relu'),
  Dense(units=16, activation='relu'),
  Dense(units=10, activation='softmax')
])
model_dnn.summary()

from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt

model_dnn.compile(loss='categorical_crossentropy', optimizer=Adam(learning_rate=0.0001), metrics=['accuracy'])
train_history_dnn = model_dnn.fit(x_train_dnn, y_train_10, validation_split=0.2, epochs=20, batch_size=1024, verbose=1)

# loss plot
plt.plot(train_history_dnn.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

# acurate plot
plt.plot(train_history_dnn.history['accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

# confusion matrix
score_dnn = model_dnn.evaluate(x_test_dnn, y_test_10) 
print("Accuracy: ", score_dnn[1]*100, '%')

results = model_dnn.predict(x_test_dnn)
results_10 = np.argmax(results, axis=1)
test_10 = np.argmax(y_test_10, axis=1)
confusion_matrix = np.zeros((10, 10), dtype=int)

for t,p in zip(test_10,results_10):
  confusion_matrix[t,p] += 1

print(confusion_matrix)
