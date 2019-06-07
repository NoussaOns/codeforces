# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 19:17:43 2019

@author: Noussa
"""

n , h = map(int,input().split())
x = list(map(int,input().split()))
res = 0

for i in x:
    if i > h:
        res += 2
    else:
        res += 1

print(res)