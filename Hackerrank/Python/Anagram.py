import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if(len(s)%2)!=0:
        return -1
    else:
        l=[0]*26
        for i in range(len(s)):
            l[ord(i)-97]+=1
        return min(l)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
