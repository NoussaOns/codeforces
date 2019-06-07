# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 20:21:51 2019

@author: Noussa
"""

n,x = map(int,input().split())

diss = 0
for i in range(n):
    p,q = input().split()   
    q = int(q)
    if p == '+':
        x += q
    elif p == '-' and x >= q:
        x -= q
    else:
        diss += 1
        continue

print(x,diss)
    