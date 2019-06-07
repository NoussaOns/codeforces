# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 17:07:48 2019

@author: Noussa
"""

l = set(input()[1:-1].split(', '))
print('0' if l == {''} else len(l))