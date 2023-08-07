#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#



def hourglassSum(arr):
    sumList = []
    for n in range(4):
        for i in range(4):
            sum = 0
            for j in range(i, i+3):
                for k in range(n, n+3):
                    if j == i+1 and (k == n or k == n+2):
                        sum += 0
                    else:
                        sum += arr[j][k]
            sumList.append(sum)
    return max(sumList)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
