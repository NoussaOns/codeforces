# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 21:25:10 2019

@author: Noussa
"""

n = int(input())
x = list(map(int,input().split()))

x.sort(reverse = False)
        
for m in x:
    print (m , end =" ")