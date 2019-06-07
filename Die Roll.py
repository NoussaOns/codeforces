# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 11:01:55 2019

@author: Noussa
"""

y,w = map(int,input().split())

maxi = max(y,w)
a = 6 - maxi + 1
b = 6


if b%a == 0 and a!= 6:
    b /= a
    a = 1
elif a % 2 ==0:
    a /= 2
    b /= 2

if a == 0:
    print("0/1")
elif a == b:
    print("1/1")
else:
    print(str(round(a))+"/"+str(round(b)))

