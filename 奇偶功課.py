# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 21:52:43 2021

@author: USER
"""

number = int(input("請輸入數字:"))
for i in range(1,number+1):
    if i % 2 != 0:
        print(i)
print("以上數字皆為奇數")    
for j in range(1,number+1):
    if j % 2 == 0:
        print(j)
print("以上數字皆為偶數")    