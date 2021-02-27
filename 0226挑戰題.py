# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:45:23 2021

@author: USER
"""

#   *                    (1,4)
#  ***              (2,3)(2,4)(2,5)
# *****        (3,2)(3,3)(3,4)(3,5)(3,6)
#*******  (4,1)(4,2)(4,3)(4,4)(4,5)(4,6)(4,7)
# *****
#  ***
#   *  
a = int(input("請輸入數字:"))
for i in range(1,2*a):     
    for j in range(1,2*a):
        if i + j > a and i + j < 3*a and j - i < a and i - j < a:
            print("*",end='')
     
        else:
            print(" ",end='')
    print()        
        
        
     