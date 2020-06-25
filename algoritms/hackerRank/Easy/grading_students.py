import math
import os
import random
import re
import sys

def gradingStudents(grades):
    # write code here
    result = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            grade = grade + 5 - (grade % 5)
        result.append(grade)
    return result

grades_count = int(input().strip())
grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print('\n'.join(map(str, result)))
print('\n')

