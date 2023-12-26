#!/bin/python3

import math
import os
import random
import re
import sys
'''
def solve(s):
    return s.title()
'''
def solve(s):
    s = re.split(" ", s)
    list_1 = []
    string = ""
    for i in s:
        if re.findall("^[a-zA-z]", i):
            list_1.append(i.capitalize())
        else:
            list_1.append(i)
    # print(s)
    # print(list_1)
    string = " ".join(tuple(list_1))
    return string
'''def solve(s):
    s=list(s)
    s.insert(0," ")
    for i in range(len(s)):
        if s[i]==" ":
            s[i+1]=s[i+1].upper()
        else:
            pass
    return "".join(s)[1:]
'''
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
