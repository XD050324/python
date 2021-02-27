# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 21:38:25 2021

@author: USER
"""

##用for迴圈印出
# 123456789
# 12345678
#     .
#     .
#     .
# 1    
for a in range(10,0,-1):
    for b in range(1,a):
        print(b,end='')
    print()