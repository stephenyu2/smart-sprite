import numpy as np

x = .33 * np.ones((1, 10), dtype = float)
y = .33 * np.ones((1, 10), dtype = float)
z = np.vstack((x, y))

def sigmoid(x):

    y = 1 / (1 + np.exp(-x))
    return y

def logit(x):

    y = np.log(x / (1 - x))
    return y

greedy = np.zeros((1, 100), dtype = int)

greedy[0, 1] = 2

n = 5
num_steps = 50
temp1 = .33 * np.ones((2, num_steps), dtype = float)
temp2 = .34 * np.ones((1, num_steps), dtype = float)
parent = np.vstack((temp1, temp2))

# int(np.where(parent[:, n] == np.max(parent[:, n]))[1][0])

print(np.where(parent[:, n] == np.max(parent[:, n]))[0][0])
