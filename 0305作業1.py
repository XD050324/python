# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:58:00 2021

@author: USER
"""

#氣泡排序法 (n個數會跑n+1次)
# a = 10
# b = 1
# if a > b:
#     temp = a
#     a = b
#     b = temp



number = list()
while len(number) <= 5:
    num = int(input("請輸入數字:"))
    number.append(num)
print("串列內容:",number)
print("氣泡排序法:")

n=0
while n <= len(number) - 1:
    for i in range(len(number)-1):
        if number[i] > number[i+1]:
            temp = number[i]
            number[i] = number[i+1]
            number[i+1] = temp
    n += 1        
print(number)   
        
        
    
    
    
    
    
    
    
    
    