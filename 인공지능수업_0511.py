# tanh 함수

import numpy as np
import matplotlib.pyplot as plt

def tanh_function(x):
    return np.tanh(x) # np는 클래스

x = np.linspace(-5, 5) # default는 100개다.
y = tanh_function(x)

plt.plot(x, y)
plt.show()

