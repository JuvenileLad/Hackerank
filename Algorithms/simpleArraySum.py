#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    ar_sum = sum(ar) 
    return ar_sum

if __name__ == '__main__':

    ar_count = 6 #int(input().strip())

    ar = [1, 2, 3, 4, 10, 11] #list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)
