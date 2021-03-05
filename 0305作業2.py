# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 20:15:22 2021

@author: USER
"""

# 樂透取號1 ~ 49亂數取6格不重複的數字並印出

import random

number = list()

while len(number) <= 5:
    n = random.randint(1,49)
    if number.count(n) > 0:
        continue
    if number.count(n) == 0:
        number.insert(0,n)

print(number)    
    