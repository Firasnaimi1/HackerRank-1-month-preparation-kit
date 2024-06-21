#!/bin/python3

import math
import os
import random
import re
import sys

""" 
Given an array of integers, where all elements but one occur twice, find the unique element.
"""

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.


"""  My solution :  """
def lonelyinteger(a):
    for i in a:
        count = a.count(i)
        if count > 1:
            continue
        else:
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
