# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 00:04:21 2019

@author: Noussa
"""
from random import randint
n,k = map(int,input().split())
dist =[]
while k > 0:
    ch = chr(randint(97,122))
    if ch not in dist:
        dist.append(ch)
        k -= 1

i = 1
s = dist[0]
while len(s) < n:
    if i < len(dist):
        if s[-1] == dist[i]:
            if i > 0:
                s+= dist[i-1]
            else:
                s += dist[i+1]
        else:
            s+= dist[i]
        i += 1
    else:
        i = 0

print(s)