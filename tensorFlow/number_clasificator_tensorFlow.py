#!/usr/bin/env python
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import clone_model
from matplotlib import pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

fig = plt.figure(figsize=(12, 12))
fig.suptitle('Dataset', fontsize=11)
timer = fig.canvas.new_timer(interval = 8000)
timer.add_callback(plt.close)
for i in range(20):
    plt.subplot(5, 4, i+1)
    plt.grid(False)
    plt.imshow(x_train[i], cmap='binary')
timer.start()
plt.show()

y_train_encoded = to_categorical(y_train)
y_test_encoded = to_categorical(y_test)

x_train_reshaped = np.reshape(x_train, (60000, 784))
x_test_reshaped = np.reshape(x_test, (10000, 784))

x_mean = np.mean(x_train_reshaped)
x_std = np.std(x_train_reshaped)

epsilon = 1e-10
x_train_norm = (x_train_reshaped - x_mean) / (x_std + epsilon)
x_test_norm = (x_test_reshaped - x_mean) / (x_std + epsilon)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model_dump = clone_model(model)
model_acc = clone_model(model)

model_dump.compile(
    optimizer='sgd',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model_acc.compile(
    optimizer='sgd',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model_dump.fit(x_train_norm, y_train_encoded, epochs=1)
model_acc.fit(x_train_norm, y_train_encoded, epochs=20)

_, accuracy_dump = model_dump.evaluate(x_test_norm, y_test_encoded)
_, accuracy_acc = model_acc.evaluate(x_test_norm, y_test_encoded)


preds_dump = model_dump.predict(x_test_norm)
preds_acc = model_acc.predict(x_test_norm)


def pred_plot(acc, preds):
    fig = plt.figure(figsize=(12,12))
    fig.suptitle(('predictions accuracy: {0}').format(acc), fontsize=11)

    for i in range(100):
        plt.subplot(10, 10, i+1)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])

        pred = np.argmax(preds[i])
        gt = y_test[i]

        col = 'g'
        if pred != gt:
            col = 'r'

        plt.xlabel('i={}, pred={}, gt={}'.format(i, pred, gt), color=col, fontsize=6)
        plt.imshow(x_test[i], cmap='binary')
    plt.show()

pred_plot(accuracy_dump, preds_dump)
pred_plot(accuracy_acc, preds_acc)


plt.figure(figsize=(6, 8))
plt.subplot(2, 1, 1)
plt.plot(preds_dump[8])
plt.xlabel("dump predictions, train=1")

plt.subplot(2, 1, 2)
plt.plot(preds_acc[8])
plt.xlabel("accurate predictions, train=20")

plt.show()
