# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:11:57 2019

@author: Noussa
"""

k,r = map(int,input().split())

n = 1
pr = n * k

while pr % 10 != 0 and pr % 10 != r:
    n += 1
    pr = n * k

print(n)