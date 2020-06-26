#!/bin/python3

import math
import os
import random
import re
import sys

def biggest_subset(list_init, k, n):
    nb_dict = dict()

    for nb in list_init:
            if nb in nb_dict:
                nb_dict[nb] += 1
            else:
                nb_dict[nb] = 1    
                
    count = n
    count_equal = 0

    for nb in nb_dict.keys():
        if k-nb == nb or nb==0:
            count -= nb_dict[nb] - 1
        elif (k-nb) in nb_dict and nb_dict[k-nb] > nb_dict[nb]:
            count -= nb_dict[nb]
        elif (k-nb) in nb_dict and nb_dict[k-nb] == nb_dict[nb]:
            count_equal += nb_dict[k-nb]
        
    return int(count - count_equal//2)

n_test, k_test = map(int, input().strip().split(' '))
list_nb = [int(x)%k_test for x in input().strip().split(' ')]

print(biggest_subset(list_nb, k_test, n_test))