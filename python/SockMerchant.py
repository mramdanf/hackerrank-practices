#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
	setOfArr = set(ar)

	total = 0
	for item in setOfArr:
		count = 0
		for i in ar:
			if item == i:
				count += 1
		if count > 1:
			total += math.floor(count / 2)

	return total

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

    # fptr.close()
