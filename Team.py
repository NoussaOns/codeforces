# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:32:27 2019

@author: Noussa
"""

n = int(input())

m = 0

for i in range(n):
    p,v,t = map(int,input().split())
    if p + v + t > 1:
        m += 1

print (m)