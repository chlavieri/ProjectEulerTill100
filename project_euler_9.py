# -*- coding: utf-8 -*-
"""
Created on Fri May  8 19:54:20 2020

@author: Carlos Henrique
"""

for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            if (a**2 + b**2 == c**2 and a < b and b < c):
                if a + b + c == 1000:
                    print(a*b*c)