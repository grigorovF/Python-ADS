#!/bin/python3

import math
import os
import random
import re
import sys



def diagonalDifference(arr):
    md = 0;
    sd = 0;
    
    n = len(arr)
    
    for i in range(n):
        md = md + arr[i][i]
        sd = sd + arr[i][n-1-i]
        
    return abs(md-sd)
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
