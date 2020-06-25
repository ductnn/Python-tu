#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cut_sticks(sticks):
    	count = 0
	if sticks:
		small_stick = min(sticks)
	else:
		return
	new_sticks = []
	for element in sticks:
		count = count + 1
		new_element = element - small_stick
		if new_element != 0:
			new_sticks.append(new_element)
	print count 
	cut_sticks(new_sticks)
		
if __name__ == '__main__':
	n = int(input())
	string = input()
	str_array = string.split(' ')
	sticks = map(lambda x: int(x), str_array)
	cut_sticks(sticks)
