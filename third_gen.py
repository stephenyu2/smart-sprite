import numpy as np
import tensorflow as tf

class neural: 

    def __init__(self, input_dim, hidden_dim = 2, mutate_threshold = .1, activation = 'relu'):

        self.best_score = 0
        self.model = None
        self.mutate_threshold = mutate_threshold
        self.hidden_dim = hidden_dim
        self.input_dim = input_dim
        self.activation = activation

    def rand_fit(self): 

        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(self.hidden_dim, 
                                  input_shape=(self.input_dim,), 
                                  activation = self.activation, 
                                  bias_initializer = 'ones'),
            tf.keras.layers.Dense(3, 
                                  bias_initializer = 'ones')

        ])



    def equal_fit(self): 

        pass ## Fits all same weights

    def update(self): 

        for i in range(2): 

            # Get weights
            weights, bias = self.model.layers[i].get_weights()

            # Mutate weights
            weights_index = np.random.rand(weights.shape[0], weights.shape[1]) < self.mutate_threshold
            weights[weights_index] = weights[weights_index] + (weights[weights_index] * np.random.uniform(-.1, .1)) 
            bias_index = np.random.rand(bias.shape[0]) < self.mutate_threshold
            bias[bias_index] = bias[bias_index] + (bias[bias_index] * np.random.uniform(-.1, .1)) 

            # Set weights
            self.model.layers[i].set_weights([weights, bias]) 

    def direction(self, inputs): 

        npinputs = np.array(inputs).reshape(1, 3) 
        if self.model == None: 

            raise ValueError("Need to run rand_fit or equal_fit before calling direction")
        
        else: 
            
            return self.model.predict(npinputs) 

    def next_gen(self): 

        pass ## Something about keeping best score