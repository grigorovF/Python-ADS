import math
import os
import random
import re
import sys

def find_closest_to_average(sequence):
    n = len(sequence)
    s = sum(sequence)

    average = s/n
    clNumber = sequence[0]
    mindiff = abs(clNumber - average)

    for num in sequence:
        dif = abs(num-average) 
        if (dif < mindiff or (dif == mindiff and num<clNumber)):
            mindiff = dif
            clNumber = num 

    return clNumber

N = int(input("Enter a number between 1-50: "))  
sequence = list(map(int, input().split())) 

print (find_closest_to_average(sequence))