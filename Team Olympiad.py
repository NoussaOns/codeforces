# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 21:33:28 2019

@author: Noussa
"""

m = int(input())
x = list(map(int,input().split()))

n = min(x.count(3),x.count(2),x.count(1))
print(n)
for i in range(n):
    i1,i2,i3 = x.index(1),x.index(2),x.index(3)
    print(i1+1,i2+1,i3+1)
    x[i1] = 0
    x[i2] = 0
    x[i3] = 0
    