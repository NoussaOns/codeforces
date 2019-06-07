# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:07:07 2019

@author: Noussa
"""
import math
n,t,k,d = map(int,input().split())
result = 'NO'
if n % k == 0:
    i = n // k
else:
    i = n // k + 1
    
one = i * t
f = 0
while i > 0 and f <= d:
    f += t
    i -= 1
    
f += t * math.floor(i/2)
s = d
s += t * round(i/2)

both = max(s,f)

if both < one:
    print('YES')
else:
    print('NO')
