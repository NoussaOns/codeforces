# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 17:45:12 2019

@author: Noussa
"""

s= input()
t = input()
p = 0
for i in t:
    if i == s[p]:
        p+=1
        
print(p+1)
