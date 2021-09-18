# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:45:34 2021

@author: Manuel
"""

class numeric_string():
    def __init__(self, Str=''):
        self.str = Str
        
        
num = numeric_string()
num2 = numeric_string('PACO')

print(num.str)
print(num2.str)
     
# =============================================================================
# 
# runfile('C:/Users/Manuel/Desktop/untitled0.py', wdir='C:/Users/Manuel/Desktop')
# Traceback (most recent call last):
# 
#   File "C:\Users\Manuel\Desktop\untitled0.py", line 15, in <module>
#     num = numeric_string()
# 
# TypeError: __init__() missing 1 required positional argument: 'const'
# 
# 
# runfile('C:/Users/Manuel/Desktop/untitled0.py', wdir='C:/Users/Manuel/Desktop')
# Traceback (most recent call last):
# 
#   File "C:\Users\Manuel\Desktop\untitled0.py", line 18, in <module>
#     num = numeric_string()
# 
# TypeError: __init__() missing 1 required positional argument: 'const'
# =============================================================================
   