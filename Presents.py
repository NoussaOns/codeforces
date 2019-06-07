# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:26:35 2019

@author: Noussa
"""

"""
n = input()

x = list(map(int,input().split()))
a = [0] * len(x)
for i in range(len(x)):
    n = x[i]
    a[n-1] = i + 1

print(*a, sep = " ")
"""

n = int(input())

lis = [int(x) for x in input().split()]

i = 1
for x in lis:
    print(lis.index(i) + 1, end= ' ')
    i += 1