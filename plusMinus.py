#!/bin/python3

import math
import os
import random
import re
import sys


def plusMinus(arr):
    positive = 0
    negative = 0
    nula = 0
    for i in range(0, len(arr)):
        if (arr[i]>0):
            positive = positive+1
        elif (arr[i]<0):
            negative = negative+1
        elif (arr[i]==0):
            nula = nula +1

    print("{:.6f}". format(positive/len(arr)))
    print("{:.6f}". format(negative/len(arr)))
    print("{:.6f}". format(nula/len(arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
