#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):
    countSpecialPalindrom = []
    for i in range(0, n):
        for j in range(0, n-i):
            subStr = s[i:n-j]
            tmpSubStr = subStr
            
            if len(subStr) % 2 != 0 and len(subStr) > 1:
                subStr = subStr[0 : (len(subStr) // 2)] + subStr[(len(subStr) // 2) + 1 : len(subStr)]
            
            allSame = True
            for k in range(0, len(subStr) - 1):
                if subStr[k] != subStr[k+1]:
                    allSame = False
                    break
            
            if allSame:
                countSpecialPalindrom.append(tmpSubStr)

    return len(countSpecialPalindrom)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    print(str(result) + '\n')

    # fptr.close()
