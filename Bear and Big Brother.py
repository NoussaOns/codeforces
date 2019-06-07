# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:27:33 2019

@author: Noussa
"""

a , b = map(int,input().split())
i = 0
while a <= b:
    a *= 3
    b *= 2
    i += 1

print(i)