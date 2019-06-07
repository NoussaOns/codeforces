# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:45:26 2019

@author: Noussa
"""

x = list(map(int,input().split()))

s = input()
ans = 0
for e in s:
    i = int(e)
    ans += x[i-1]

print(ans)
        