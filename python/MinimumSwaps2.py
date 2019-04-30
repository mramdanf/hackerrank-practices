#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
	n = len(arr)
	swaps = 0
	for i in range(0, n - 1):
		while arr[i] != i + 1:
			t = arr[arr[i] - 1]
			arr[arr[i] - 1] = arr[i]
			arr[i] = t
			swaps += 1
			print(arr)
		print()
	return swaps

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')

    # fptr.close()
