# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:43:01 2021

@author: USER
"""

#使用者輸入數值,做1~?數字的總和

a = int(input("請輸入數字:"))
i = total = 0
while i < a:
    i+=1
    total += i
print(total) 