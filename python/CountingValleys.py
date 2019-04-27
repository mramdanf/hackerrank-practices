#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
	current, valleyCount = 0,0

	for item in s:
		if item == 'U':
			current += 1
			if current == 0:
				valleyCount += 1
		else:
			current -= 1
	
	return valleyCount

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')

    # fptr.close()
