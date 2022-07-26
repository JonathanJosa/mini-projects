from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Softmax, Conv2D, MaxPooling2D

model = Sequential()

model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(16, activation='relu', name='dense_layer_1'))
model.add(Dense(16, activation='relu'))
#model.add(Dense(10, activation='softmax'))
model.add(Dense(10))
model.add(Softmax())

model.weights
model.summary()


model_cov = Sequential([
    Conv2D(16, kernel_size=(3,3), padding='SAME', strides=2, activation='relu', input_shape=(28, 28, 3), data_format='channel_last'),  # input shape must be 3 dimensions
    MaxPooling2D(pool_size=(3, 3)),
    Flatten(),
    Dense(16, activation='relu'),
    Dense(10, activation='softmax'),
])

model_cov.weights
model_cov.summary()
