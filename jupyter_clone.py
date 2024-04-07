from game import game
from third_gen import neural

# Game initialization
# level1 = game() 
# level1.start(level = 1) 

# Model initialization
# neural_test = neural(input_dim = level1.get_input_dimension(), hidden_dim = 2, mutate_threshold = .1)
neural_test = neural(input_dim = 3, hidden_dim = 2, mutate_threshold = .1)
neural_test.rand_fit() 
neural_test.update() 
neural_test.update() 
neural_test.update() 

# reward = level1.play_epoch(neural_test)
# print(reward) 