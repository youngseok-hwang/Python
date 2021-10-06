# Softmax 함수

import numpy as np
import matplotlib.pyplot as plt

def softmax_function(x):
    z = np.exp(x)/np.sum(np.exp(x))
    return z
x = np.array([1,2,3])
y = softmax_function(x)
print(y)