# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:55:25 2021

@author: USER
"""

number = int(input("請輸入數字:"))
a = 0
for j in range(1,number+1):
    if j % 2 == 0:
        a += j
print(a)   