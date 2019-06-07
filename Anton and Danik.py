# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 20:19:35 2019

@author: Noussa
"""

n = int(input())
s = input()

a = 0
d = 0
for i in s:
    if i == 'D':
        d += 1
    if i == 'A':
        a += 1
        
if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')