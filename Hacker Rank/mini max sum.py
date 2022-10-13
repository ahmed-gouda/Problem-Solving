#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    mi=0
    ma=0
    for i in range( 0, len(arr)-1):
        mi+=arr[i] 
    for i in range( 1, len(arr)):
        ma+=arr[i] 
    print(str(mi)+" "+str(ma))      
                

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
