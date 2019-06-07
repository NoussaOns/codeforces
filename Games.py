# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 14:54:03 2019

@author: Noussa
"""

n = int(input())
ans = 0
h = []
g = []

for i in range(n):
    h1,g1 = map(int,input().split())
    h.append(h1)
    g.append(g1)

for e1 in h:
    for e2 in g:
        if e1 == e2:
            ans += 1

print(ans)