import numpy as np
from TwoLayerNet import TwoLayerNet

# 5.7.4 ---------------------------
from DataSet.mnist import load_mnist

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

train_loss_list = []

iters_num = 1000
train_size = x_train.shape[0]
batch_size = 100
learning_rate = 0.1
net = TwoLayerNet(input_size=784, hidden_size=50,output_size=10)

for i in range(iters_num):
    batch_mask = np.random.choice(train_size, batch_size)
    x_batch = x_train[batch_mask]
    t_batch = t_train[batch_mask]

    grad = net.gradient(x_batch, t_batch)

    for key in ('W1', 'b1', 'W2', 'b2'):
        net.params[key] -= learning_rate * grad[key]

    loss = net.loss(x_batch, t_batch)
    train_loss_list.append(loss)


import matplotlib.pyplot as plt

plt.plot(range(len(train_loss_list)), train_loss_list)
plt.show()