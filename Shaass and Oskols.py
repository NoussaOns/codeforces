# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 12:16:38 2019

@author: Noussa
"""

n = int(input())
a = list(map(int,input().split()))
m = int(input())

for i in range(m):
    x,y= map(int,input().split())
    x -= 1
    if x > 0:
        a[x-1] += y - 1
    if x < len(a) - 1:
        a[x+1] += a[x] - y
    a[x] = 0
    
for i in a:
    print(i)