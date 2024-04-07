import numpy as np
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(2, input_shape=(3,), activation='relu'),
    tf.keras.layers.Dense(3)
])

index = np.random.rand(3, 2) < .1
print(index) 

weights, biases = model.layers[0].get_weights()
print(weights)
print(biases) 
print(weights.shape[0])
print(biases.shape)

weights[index] = weights[index] + (weights[index] * np.random.uniform(-.1, .1)) 
print(weights)

print(np.random.rand(2)) 

for i in range(1): 

    print(i)