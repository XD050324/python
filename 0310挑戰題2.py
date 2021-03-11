# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:55:08 2021

@author: USER
"""

'''
      1           0
    1  1         0 1  
  1  2  1       0 1 2 
1  3  3  1     0 1 2 3
.             0 1 2 3 4
.
.
'''
n = int(input('請輸入數字:'))
x = [1]
y = [1,1]
print('{:<3d} '.format(1))
print('{:<3d} {:<3d}'.format(1,1))
for i in range(2,n):
    for j in range(i - 1):
         c = y[j] + y[j + 1]
         y.append(c)
    del y[0:i]
    y.insert(i - 1,1)
    y.insert(0,1)
    for k in y:
        print('{:<3d} '.format(k),end='')
    print()        
    
    


'''
del x[0:i]
x.insert(i - 1,1)
x.insert(0,1)
 '*(n - i + 1),k,' ',end=''
'''







