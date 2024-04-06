import numpy as np
import tensorflow as tf

class neural: 

    def __init__(self, mutate = .1):

        self.best_score = 0
        self.model = None
        self.mutate = mutate

    def rand_fit(self): 

        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(2, input_shape=(3,), activation='relu'),
            tf.keras.layers.Dense(3)
        ])

    def equal_fit(self): 

        pass ## Fits all same weights

    def update(self): 

        pass ## Mutates a new NN

    def direction(self, inputs): 

        npinputs = np.array(inputs).reshape(1, 3) 
        if self.model == None: 

            raise ValueError("Need to run rand_fit or equal_fit before calling direction")
        
        else: 
            
            print(self.model.predict(npinputs) )
            return self.model.predict(npinputs) 

    def next_gen(self): 

        pass ## Something about keeping best score