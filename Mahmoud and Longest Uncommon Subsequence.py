# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:33:27 2019

@author: Noussa
"""

import itertools as it


a = input()
b = input()

print(-1 if a == b else max(len(a),len(b)))