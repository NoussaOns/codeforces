# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 00:25:43 2019

@author: Noussa
"""

a = input()

x = []

for i in a:
    if i.isupper():
        x.append(i)

if len(x) > len(a) / 2:
    print(a.upper())

else:
    print(a.lower())