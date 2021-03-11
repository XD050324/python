# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:51:20 2021

@author: USER
"""

# 2/1,3/2,5/3,8/5,13/8,21/13 前20項之和

n = int(input('請輸入數字:'))
x = [1,1]
a = 1
b = 1
for i in range(n):
    c = a + b
    a = b
    b = c
    x.append(c)

d = 0

for i in range(n):
    e = x[i + 2] / x[i + 1]
    d += e
print(d)    
    
    
   










  