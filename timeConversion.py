#!/bin/python3

import math
import os
import random
import re
import sys



def timeConversion(s):
    hour = s[:2]
    minsec = s[2:8]
    ampm = s[-2:]
    
    
    hh = int(hour)
    
    if (ampm == 'AM'):
        if (hh==12):
            hour = '00'
            
    elif(ampm == 'PM'):
        if (hh != 12):
            hh = hh+12
        hour = str(hh)
       
    
    
    hour = f"{int(hour):02}"
    return hour + minsec
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
