# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:22:52 2019

@author: Noussa
"""

x = list(map(int,input().split()))
u = []
for e in x:
    if e not in u:
        u.append(e)
        
print(4-len(u))