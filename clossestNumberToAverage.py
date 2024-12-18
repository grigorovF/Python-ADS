import math
import os
import random
import re
import sys

def find_closest_to_average(sequence):
    n = len(sequence)
    s = sum(sequence)
    arr = []
    arr = sequence.sort()
    average = s/n
    
    minNumber = sequence[0] 

    return arr

N = int(input("Enter a number between 1-50: "))  
sequence = list(map(int, input().split())) 

print (find_closest_to_average(sequence))