#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'longestChain' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY words as parameter.
#

def longestChain(words):
    # Write your code here
	resCount = []
	for i in words:
		if len(i) > 1:
			count = 0
			for j in words:
				if i != j:
					allIn = True
					for charJ in j:
						if i.find(charJ) == -1:
							allIn = False
					if allIn:
						count += 1
						print(i, end=' ')
						print(j, end=' ')
						print(count)
			resCount.append(count)
	return max(resCount)
			



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    result = longestChain(words)

    print(str(result) + '\n')

    # fptr.close()
