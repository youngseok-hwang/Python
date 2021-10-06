
import numpy as np
import matplotlib.pyplot as plt

# 입력 준비
input_data = np.arange(0, np.pi*2, 0.1)
correct_data = np.sin(input_data)  # 타겟
input_data = (input_data - np.pi)/np.pi  # 정규화(-1 ~ 1.0)
n_data = len(correct_data)

# 뉴런 수 정리
n_in = 1
n_mid = 3
n_out = 1

wb_width = 0.01
eta = 0.1  # 적당히 조절할 것, 너무 키우면 발산됨
epoch = 2001  # 반복하는 것
interval = 200  # 표시관계, 200개당 1묶음씩 잘 되는지 안되는지 표시하는 것


class MiddleLayer: # 은닉층
    def __init__(self, n_upper, n):
        self.w = wb_width*np.random.randn(n_upper, n)
        self.b = wb_width*np.random.randn(n)

    def forward(self, x):
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = 1/(1 + np.exp(-u)) # sigmoid activation function

    def backward(self, grad_y):
        delta = grad_y * (1-self.y) * self.y
        self.grad_w = np.dot(self.x.T, delta)
        self.grad_u = np.sum(delta, axis=0) # axis = 0은 행으로 간다는 의미

        self.grad_x = np.dot(delta, self.w.T)

    def update(self, eta):
        self.w -= eta*self.grad_w
        self.b -= eta*self.grad_b


class OutputLayer: # 출력층
    def __init__(self, n_upper, n):
        self.w = wb_width * np.random.randn(n_upper, n)
        self.b = wb_width * np.random.randn(n)

    def forward(self, x):   # 순전파
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = u

    def backward(self, t):  # 역전파
        delta = self.y - t  # 회귀 문제 기울기 구하기

        self.grad_w = np.dot(self.x.T, delta)  # grad: 편미분, T: 트랜스펄션
        self.grad_b = np.sum(delta, axis = 0)

        self.grad_x = np.dot(delta, self.w.T)

    def update(self, eta):  # eta: 갱신율
        self.w -= eta * self.grad_w # self.w = self.w - eta * self.grad_w
        self.b -= eta * self.grad_b # self.b = self.b - eta * self.grad_b

# == 각 층의 초기화 --
middle_layer = MiddleLayer(n_in, n_mid)
output_layer = OutputLayer(n_mid, n_out)

# learning
for i in range(epoch):

    # 인덱스 섞기
    index_random = np.arange(n_data)
    np.random.shuffle(index_random)  # shuffle: 섞기 => 데이터가 한 쪽으로 몰리지 않게 만들어 줌

    # 결과 표시
    total_error = 0
    plot_x = []
    plot_y = []

    for idx in index_random:
        x = input_data[idx:idx+1]
        t = correct_data[idx:idx+1]

        middle_layer.forward(x.reshape(1,1))
        output_layer.forward(middle_layer.y)

        output_layer.backward(t.reshape(1,1))
        middle_layer.backward(output_layer.grad_x)

        middle_layer.update(eta)
        output_layer.update(eta)

        if i%interval == 0:
            y = output_layer.y.reshape(-1)

            total_error = total_error + 1.0/2.0 * np.sum(np.square(y - t))

            plot_x.append(x)
            plot_y.append(y)

        if i%interval == 0:
            plt.plot(input_data, correct_data, linestyle ="dashed")
            plt.scatter(plot_x, plot_y, marker = "+")
            plt.show()

            print("Epoch:" + str(i) + "/" + str(epoch),
                  "Error" + str(total_error/n_data))
