# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 20:51:16 2019

@author: Noussa
"""

x = input().split('+')
x.sort()
i=0
for e in x:
    i += 1
    if i != len(x):
        print(e,end='+')
    else:
        print(e,end='')