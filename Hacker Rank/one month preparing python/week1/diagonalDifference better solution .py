#!binpython3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr)
    dif=0
    n=len(arr)-1
    b=-1
    while(n!=-1)
        b+=1
        dif+=arr[n][n]-arr[b][n]
        n-=1
    return abs(dif) 
        

if __name__ == '__main__'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n)
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + 'n')

    fptr.close()
