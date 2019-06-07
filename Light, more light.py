# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 07:49:03 2019

@author: Noussa
"""
import math
done = False
x=[]
while not done:
    n = int(input())
    if n != 0:
        print('yes' if math.floor(math.sqrt(n)) == math.ceil(math.sqrt(n)) else 'no')
    else:
        done = True
