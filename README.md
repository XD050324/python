# python# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:40:08 2021

@author: USER
"""

#請輸入猜值~猜值之間的數字

import random
count = 0
ans = random.randint(1,100)
guess = 0
a = 1
b = 100

while ans != guess:
    print("請輸入",a,"~",b,"之間的數字:",sep="")
    guess = int(input())
    if ans > guess:
        a = guess + 1        
    elif  ans < guess:
        b = guess - 1
    count += 1
print("猜對了!花費次數:",count)        
