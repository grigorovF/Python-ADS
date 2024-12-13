
import math
import os
import random
import re
import sys



def compareTriplets(a, b):
    gA=0;
    gB=0;
    for i in range(0,3):
        if(a[i]> b[i]):
            gA = gA + 1
        elif(a[i]< b[i]):
            gB = gB+1

    return [gA, gB]
        

        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
