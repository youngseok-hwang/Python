# ReLU 함수

import numpy as np
import matplotlib.pyplot as plt

def relu_fuction(x):
    return np.where(x<=0, 0.01*x, x) # 0보다 작거나 같은 것은 0, 아닌 것은 x 그대로

x = np.linspace(-6, 5)
y = relu_fuction(x)

plt.plot(x,y)
plt.show()