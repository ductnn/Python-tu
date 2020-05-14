import pandas as pd
import numpy as np
import matplotlib as plt

X = np.array([[150, 152, 160, 163, 170, 175, 180, 190]]).T
Y = np.array([[40, 42, 44, 45, 55, 58, 60, 75]])

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis=1)
