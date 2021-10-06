
# 실체가 손에 잡히는 딥러닝 P.160

import numpy as np
import matplotlib.pyplot as plt

# Input value
X = np.arange(-1.0, 1.0, 0.1)
Y = np.arange(-1.0, 1.0, 0.1)

# Weighting
W_im = np.array([[1.0, 2.0],
                 [2.0, 3.0]])
W_mo = np.array([[-1.0, 1.0],
                 [1.0, -1.0]])

b_im = np.array([0.3, -0.3])
b_mo = np.array([0.4, 0.1])

# Layer definition
def middle_layer(x, w, b):
    u = np.dot(x, w) + b   # 행렬이어서 dot()을 써서 곱해줌
    return 1/(1 + np.exp(-u))

def output_layer(x, w, b):
    u = np.dot(x, w) + b
    return np.exp(u)/np.sum(np.exp(u))

x_1 = []
y_1 = []
x_2 = []
y_2 = []

# 각 그리드 별 신경망 연산
for i in range(20):
    for j in range(20):

        inp = np.array([Y[i], Y[j]])
        mid = middle_layer(inp, W_im, b_im)
        out = output_layer(mid, W_mo, b_mo)  # 출력층의 입력은 은닉층의 출력

        if out[0] > out[1]:
            x_1.append(X[i])
            y_1.append(Y[j])
        else:
            x_2.append(X[i])
            y_2.append(Y[j])

plt.scatter(x_1, y_1, marker = "+") # scatter() 점으로 흩뿌리는 거
plt.scatter(x_2, y_2, marker = "o")
plt.show()

# im = input_layer -> middle_layer
# mo = middle_layer -> output_layer

