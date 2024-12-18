#!/bin/python3

import math
import os
import random
import re
import sys


def matchingStrings(stringList, queries):
    matches = []
    for string1 in stringList:
        count = 0
        for query in queries:
            if (query == string1):
                count += 1
        matches.append(count)
    return matches 

         

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
