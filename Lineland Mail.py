# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:16:12 2019

@author: Noussa
"""

n = int(input())

x = [int(c) for c in input().split()]

print(x[1] - x[0], x[len(x) - 1] - x[0])

for i in range(1,n-1):
    l = x[i] - x[i-1]
    r = x[i+1] - x[i]
    print (min(l,r), end= " ")
    
    l = x[i] - x[0]
    r = x[len(x)-1] - x[i]
    print (max(l,r))
    
print(x[len(x)-1] - x[len(x)-2] , x[len(x)-1] - x[0])
