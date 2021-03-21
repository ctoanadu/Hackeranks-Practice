
import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxx=-float('inf')
    for i in range(4):
        for j in range(4):
            summ=0
            summ=summ + arr[i][j]+arr[i][j+1]+arr[i][j+2]
            summ=summ + arr[i+1][j+1]
            summ=summ + arr[i+2][j]+ arr[i+2][j+1]+arr[i+2][j+2]
            if summ>maxx:
                maxx=summ
    return maxx
    return summ

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
