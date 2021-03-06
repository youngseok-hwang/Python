# Softmax 함수

import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-1.0, 1.0, 0.2)
Y = np.arange(-1.0, 1.0, 0.2)
Z = np.zeros((10,10))

w_x = 2.5
w_y = 3.0
bias = 0.1

for i in range(10):
    for j in range(10):

        u = X[i]*w_x +Y[j]*w_y + bias

        y = 1/(1 + np.exp(-u))
        Z[j][i] = y

plt.imshow(Z, "gray", vmin = 0.0, vmax = 1.0)
plt.colorbar()
plt.show()

