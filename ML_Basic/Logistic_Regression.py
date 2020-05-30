from __future__ import division, print_function, unicode_literals
import numpy as np
import matplotlib as plt

X = np.array([[0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50]]).T
y = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1])

def sigmoid(S):
    return 1/(1 + np.exp(-S))

def prob(w, X):
    return sigmoid(X.dot(w))

def loss(w, X, y, lamda):
    z = prob(w, X)
    return -np.mean(y*np.log(z) - (1-y)*np.log(1-z)) + 0.5*lamda/X.shape[0]*np.sum(w*w)

def logistic_regression(w_init, X, y, lam = 0.001, learn_rate = 0.1, max_count = 2000):
    N, d = X.shape[0], X.shape[1]
    w = w_old = w_init
    loss_hist = [loss(w_init, X, y, lam)] # store history of loss in loss_hist
    for i in range(max_count):
        mix_ids = np.random.permutation(N)
        for j in mix_ids:
            xj = X[j]
            yj = y[j]
            zj = sigmoid(xj.dot(w))
            w = w - learn_rate*((zj - yj)*xj + lam*w)
        loss_hist.append(loss(w, X, y, lam))
        if np.linalg.norm(w - w_old)/d < 1e-6:
            break
        w_old = w
    return w, loss_hist

N = X.shape[0]
Xbar = np.concatenate((X, np.ones((N, 1))), axis = 1)
w_init = np.random.randn(Xbar.shape[1])
lam = 0.0001
w, loss_hist = logistic_regression(w_init, Xbar, y, lam, learn_rate = 0.05, max_count = 500)
print(w)
print(loss(w, Xbar, y, lam))
