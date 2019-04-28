#!/bin/python3

import math
import os
import random
import re
import sys

def countAFrontString(s):
	countA = 0
	for item in s:
		if item == 'a':
			countA += 1
	return countA

# Complete the repeatedString function below.
def repeatedString(s, n):
	return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")
	

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')

    # fptr.close()
