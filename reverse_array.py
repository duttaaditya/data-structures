import math
import os
import random
import re
import sys


def reverseArray(a):
    # Write your code here
    l = len(a)
    b = []
    
    for i in range(1,l+1):
        j = a.pop(l-i)
        b.append(j)
    return b         


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split())) # 1 2 4 6 --> [1, 2, 4, 6]
    res = reverseArray(arr)
    print(' '.join(map(str, res)))