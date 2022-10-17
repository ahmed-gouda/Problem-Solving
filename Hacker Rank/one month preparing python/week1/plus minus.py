#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pls=0
    mns=0
    zeros=0
    for i in arr:
        if i >0:
            pls+=1
        elif i<0:
            mns+=1
        else:
            zeros+=1
    print( "%0.6f"%(float(pls)/len(arr)),"\n%0.6f"%(float(mns)/len(arr)),"\n%0.6f"%(float(zeros)/len(arr)))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    (plusMinus(arr))
