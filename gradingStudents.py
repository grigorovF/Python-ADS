
import math
import os
import random
import re
import sys
    

def gradingStudents(grades):
    rounded = []
    for grade in grades:
        if (grade<38 or grade%5<3):
            rounded.append(grade)
        else:
            dif = grade + (5-grade%5)
            rounded.append(dif)
    return rounded

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
