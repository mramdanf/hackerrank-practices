#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
	arr = [0]*n
	for i in queries:
		a,b,k = i[0],i[1],i[2]
		arr[a - 1] += k
		if b != len(arr):
			arr[b] -= k

	maxval = 0
	itt = 0
	for q in arr:
		itt += q
		if itt > maxval:
			maxval = itt
	return maxval


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')

    # fptr.close()
