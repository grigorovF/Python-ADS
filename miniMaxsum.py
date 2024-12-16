#!/bin/python3

import math
import os
import random
import re
import sys



def miniMaxSum(arr):
    defArr = arr.sort()
    maxArr = sum(arr[1::])
    minArr = sum(arr[::-1])

    print(minArr, maxArr)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
