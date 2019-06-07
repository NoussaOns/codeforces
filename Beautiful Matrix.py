# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:47:52 2019

@author: Noussa
"""

i = 0
j = 0
c1 = 0
for m in range(5):
    x = list(map(int,input().split()))
    c1 += 1
    c2 = 0
    for k in x:
        c2 += 1
        if k == 1:
            i = c1
            j = c2
            break
print (abs(3 - i) + abs(3-j))