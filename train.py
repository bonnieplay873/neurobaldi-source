from nn import create_model
import numpy as np

data = []
for i in range(10000):
    state = np.random.rand(8)
    action = np.random.randint(0, 2)
    data.append((state, action))