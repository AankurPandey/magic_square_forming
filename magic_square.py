import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    data=[[[4,9,2],[3,5,7],[8,1,6]],
          [[2,9,4],[7,5,3],[6,1,8]],
          [[2,7,6],[9,5,1],[4,3,8]],
          [[6,7,2],[1,5,9],[8,3,4]],
          [[8,1,6],[3,5,7],[4,9,2]],
          [[6,1,8],[7,5,3],[2,9,4]],
          [[8,3,4],[1,5,9],[6,7,2]],
          [[4,3,8],[9,5,1],[2,7,6]]]
    c=[]
    
    for i in data:
        SU=0
        for j in range(3):
            k=0
            for k in range(3):
                if s[j][k]>i[j][k]:
                    SU+=s[j][k]-i[j][k]
                else:
                    SU+=i[j][k]-s[j][k]
        c.append(SU)
    c.sort()
    return c[0]    
           
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
