#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def maxDifference(a):
    # Write your code here
    minVal, maxVal, maxDiff = a[0], a[0], -1

    for i in range(1, len(a)):
        minVal = min(a[i], minVal)
        if a[i] > maxVal:
            maxDiff = max(maxDiff, a[i] - minVal)
            maxVal = a[i]

    return maxDiff

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = maxDifference(a)

    print(str(result) + '\n')

    # fptr.close()
