#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
	n = len(c) - 1
	i = 0
	path = []

	while i < n:
		if (i + 2) <= n and c[i + 2] == 0:
			path.append(i + 2)
			i += 2
		else:
			path.append(i + 1)
			i += 1
	
	return len(path)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')

    # fptr.close()
