#!/bin/python3

import math
import os
import random
import re
import sys

# 5
# 2 1 5 3 4
# 0 1 2 3 4
# ans=3

# i=4
# ans=1
# 4 - (4 + 1) > 2 ? false
# range(max(0, 2), 4) -> 2 - 3
#  if 5,3 > 4


# i=3
# ans=2
# 3 - (3 + 1) > 2 ? false
# range(max(0, 1), 3) -> 1 - 2
#  if 1,5 > 3

# i=2
# ans=2
# 5 - (2 + 1) > 2 ? false
# range(max(0, 3), 2) -> 3 - 2

# i=1
# ans=3
# 1 - (1 + 1) > 2 ? false
# range(max(0, -1), 1) -> 0 - 1
#  if 2,1 > 1

# i=0
# ans=3
# 2 - (0 + 1) > 2 ? false
# range(max(0, 0), 0) -> 0 - 0


# Complete the minimumBribes function below.
def minimumBribes(q):
	ans = 0
	for i in reversed(range(0, len(q))):
		if q[i] - (i + 1) > 2:
			print('Too chaotic')
			return
		for j in range(max(0, q[i] - 2), i):
			if q[j] > q[i]:
				ans += 1
	print(ans)
		


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
