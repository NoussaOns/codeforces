# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 22:23:38 2019

@author: Noussa
"""

a = int(input())

pre = -1
ans = 0
for i in range(a):
    x = input()
    if x != pre:
        ans += 1
    pre = x
    
print(ans)