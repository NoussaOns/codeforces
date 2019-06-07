# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 22:37:46 2019

@author: Noussa
"""

s = input()
ans = 0
#coefficient
c = 0


for l in s:
    i = ord(l) - 97 + c
    if l == 'a':
        i = 26 + c
    if 26 - i < i:
        ans += 26 - i
        c += 26 - i
    else:
        ans += i
        c += -i
        
print(ans)