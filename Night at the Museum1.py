# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 00:19:17 2019

@author: Noussa
"""

s = input()
ans = 0
start = 0


for l in s:
    i = ord(l) - 97
    walk = abs(start-i)
    if walk < 13:
        ans += walk
    else:
        ans += 26 - walk
    start = i
        
print(ans)