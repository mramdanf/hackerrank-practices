#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    res = []
    for i in range(d, n):
      res.append(a[i])
    
    if d != 0:
      for i in range(0, d):
        res.append(a[i])
    
    print(" ".join(map(str, res)))