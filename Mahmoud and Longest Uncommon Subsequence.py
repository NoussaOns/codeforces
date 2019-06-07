# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:33:27 2019

@author: Noussa
"""

import itertools as it


a = input()
b = input()
s = ""
x = []
l1 = -2
for i in reversed(range(0,len(a)+1)):
    x = list(it.combinations(a,i))
    for e in x:
        s = ''.join(e)
        if s not in b and b not in s:
            l1 = len(s)
            break
    if l1 > 0:
        break
    else:
        l1 = -1
  
l2 = -2
for i in reversed(range(0,len(b)+1)):
    x = list(it.combinations(b,i))
    for e in x:
        s = ''.join(e)
        if s not in a and a not in s:
            l2 = len(s)
            break
    if l2 > 0:
        break
    else:
        l2 = -1
        
print(max(l1,l2))


"""

def uncommon(a,b):
 """   