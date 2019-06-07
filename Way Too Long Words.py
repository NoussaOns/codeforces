# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:10:59 2019

@author: Noussa
"""

n = int(input())
x = []

for i in range(n):
    word = input()
    if len(word)>10:
        f = word[0]
        l = word[-1]
        length = len(word[1:-1])
        x.append(f+str(length)+l)
    else:
        x.append(word)
    
for e in x:
    print(e)
    
    