import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

Dataset = pd.read_excel('iris.xlsx')
# Dataset = pd.DataFrame(Dataset)

X = Dataset[['X1', 'X2', 'X3', 'X4']]
X = np.array(X)
# ones = np.ones((X.shape[0],1))
# X = np.concatenate((X,ones), axis =1)

# K = 3

center = np.array([])
K = 3

# for i in range(K):
#     center = np.append(center, X[i], axis=0)
#     cluster.append([])

# center = center.reshape(K, 2)
# Y = Dataset.values[: ,4]
# Y = Y.reshape(Y.shape[0], 1)
# sentosa = np.random.permutation(range(1, 51))
# versicolor = np.random.permutation(range(51, 101))
# virginica = np.random.permutation(range(101, 151))
# Train_Sentosa = sentosa[:15]
# Test_Sentosa = sentosa[15:50]

def init(X, K):
    # randomly pick k rows of X as initial centers
    return X[np.random.choice(X.shape[0], K, replace=False)]

def group(X, center):
    y = np.zeros(X.shape[0])
    for i in range(X.shape[0]):
        d = X[i] - center
        d = np.linalg.norm(d, axis=1)
        y[i] = np.argmin(d)

    return y

def update(X, y, K):
    center = np.zeros((K, X.shape[1]))
    for i in range(K):
        Xi = X[y==i, :]
        center[i, :] = np.mean(Xi, axis=0)

    return center

# def converged(center, new_center):
#     # return True if two sets of centers are the same
#     return (set([tuple(a) for a in center]) ==
#         set([tuple(a) for a in new_center]))
#
def kmeans(X, K):
    center = [init(X, K)]
    y = []
    count = 0
    while True:
        # y.append(group(X, center[-1]))
        # new_center = update(X, y[-1], K)
        # if converged(center[-1], new_center): break
        # center.append(new_center)
        # count+=1
        # center = update(X, y,  K)

        #Đoạn này cop bất lực
        y_old = y
        # grouping
        y = group(X, center)
        # break while loop if groups are not changed
        if np.array_equal(y, y_old):
            break
        #  update centers
        center = update(X, y, K)
        count+=1
    return(center, y)

for i in range(len(X)):
    kmeans(X, K)
    print(center)
