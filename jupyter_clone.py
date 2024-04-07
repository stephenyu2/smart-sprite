import numpy as np
from game import game
from third_gen import neural

# Game initialization
level1 = game() 
level1.start(level = 1) 

# Model initialization
np.random.seed(100) 
neural_test = neural(input_dim = level1.get_input_dimension(), hidden_dim = 2, mutate_threshold = .1)
neural_test.rand_fit() 

best_reward = 0
for i in range(50): 

    neural_test.update() 
    reward = level1.play_epoch(neural_test) 

    if reward > best_reward: 

        reward = best_reward
        best_neural = neural_test

print(best_reward) 

level1.play_epoch(best_neural) 