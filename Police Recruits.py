# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 00:27:51 2019

@author: Noussa
"""

a = input()
x = list(map(int,input().split()))

# hired h untreated u
h = u = 0
for e in x:
    if e > 0:
        h+=e
        continue
    if e < 0 and h > 0:
        h -= 1
        continue
    if e < 0 and h < 1:
        u += 1

print(u)
        