# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 20:32:01 2019

@author: Noussa
"""

a = input()
s = input()

p = s[0]
st = 0

for l in s[1:]:
    if l == p:
        st += 1
    p = l
    
print(st)