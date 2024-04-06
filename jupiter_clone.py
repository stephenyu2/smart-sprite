from game import game

## game initialization

level1 = game() 
level1.start(level = 1) 
reward = level1.play_epoch()
print(reward) 