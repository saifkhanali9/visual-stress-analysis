import keras
from keras.models import Sequential
from keras.layers import Dense


# Data part

# model
model = Sequential()
model.add(Dense(512, input_dim=200*8, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(2, actiavtion = 'softmax'))

# compilation
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# fit model
training = model.fit(X_train, y_train, epochs=100, batch_size=32)

# predictions
predictions = model.predict(X_test)
